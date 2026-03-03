#!/usr/bin/env node
/**
 * Daily PR Report Generator
 *
 * Improvements over v1:
 * - Two-phase query: bulk basic data first, CI status fetched individually (avoids timeouts)
 * - Context carryover: reads yesterday's report so Claude can note what changed
 * - Smarter PR categorization: failing CI, stale, WIP detection
 * - Fully hyperlinked PR references in output
 * - Staleness detection (3+ days no activity)
 * - "Do Not Review / WIP" detection for non-draft PRs
 */

const { Octokit } = require('@octokit/rest');
const Anthropic = require('@anthropic-ai/sdk');
const fs = require('fs');
const path = require('path');

const octokit = new Octokit({ auth: process.env.GITHUB_TOKEN });
const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY || "dummy",
  baseURL: process.env.ANTHROPIC_BASE_URL,
  defaultHeaders: {
    ...(process.env.AMD_LLM_GATEWAY_KEY && {
      "Ocp-Apim-Subscription-Key": process.env.AMD_LLM_GATEWAY_KEY,
    }),
  },
});

const OWNER = process.env.REPO_OWNER || 'ROCm';
const REPO = process.env.REPO_NAME || 'rocm-systems';
const REPO_URL = `https://github.com/${OWNER}/${REPO}`;
const PR_LABEL = process.env.PR_LABEL || 'project: rocprofiler-systems';

// ── Phase 1: Bulk fetch basic PR data (fast, no timeouts) ─────────────────────

async function getOpenPRs() {
  const allPRs = [];
  let page = 1;
  while (true) {
    const { data } = await octokit.pulls.list({
      owner: OWNER, repo: REPO, state: 'open', per_page: 100, page,
      labels: PR_LABEL,
    });
    allPRs.push(...data);
    if (data.length < 100) break;
    page++;
  }
  console.log(`Found ${allPRs.length} open PRs with label "${PR_LABEL}"`);
  return allPRs;
}

// ── Phase 2: Per-PR enrichment (CI queried individually to avoid timeouts) ────

async function getCIStatus(headSha) {
  try {
    const { data } = await octokit.checks.listForRef({
      owner: OWNER, repo: REPO, ref: headSha, per_page: 50,
    });
    if (data.check_runs.length === 0) return { overall: 'no_checks', failing: [], inProgress: [] };

    const failing = data.check_runs.filter(r => ['failure', 'timed_out'].includes(r.conclusion));
    const inProgress = data.check_runs.filter(r => r.status !== 'completed');
    const allPassed = data.check_runs.every(r => ['success', 'skipped', 'neutral'].includes(r.conclusion));

    let overall;
    if (inProgress.length > 0) overall = 'in_progress';
    else if (failing.length > 0) overall = 'failing';
    else if (allPassed) overall = 'passing';
    else overall = 'unknown';

    return {
      overall,
      failing: failing.map(r => r.name),
      inProgress: inProgress.map(r => r.name),
    };
  } catch {
    return { overall: 'unavailable', failing: [], inProgress: [] };
  }
}

async function getReviewInfo(prNumber) {
  try {
    const { data: reviews } = await octokit.pulls.listReviews({
      owner: OWNER, repo: REPO, pull_number: prNumber,
    });
    const latestByUser = {};
    for (const review of reviews) {
      if (review.state !== 'COMMENTED') latestByUser[review.user.login] = review.state;
    }
    const states = Object.values(latestByUser);
    let reviewDecision = 'pending';
    if (states.includes('CHANGES_REQUESTED')) reviewDecision = 'changes_requested';
    else if (states.includes('APPROVED')) reviewDecision = 'approved';
    return {
      reviewDecision,
      approvedBy: Object.entries(latestByUser).filter(([, s]) => s === 'APPROVED').map(([u]) => u),
      changesRequestedBy: Object.entries(latestByUser).filter(([, s]) => s === 'CHANGES_REQUESTED').map(([u]) => u),
    };
  } catch {
    return { reviewDecision: 'unknown', approvedBy: [], changesRequestedBy: [] };
  }
}

async function getLatestCommit(prNumber) {
  try {
    const { data } = await octokit.pulls.listCommits({
      owner: OWNER, repo: REPO, pull_number: prNumber, per_page: 100,
    });
    if (!data.length) return null;
    const last = data[data.length - 1];
    return {
      sha: last.sha.substring(0, 7),
      message: last.commit.message.split('\n')[0].substring(0, 80),
      date: last.commit.author.date,
      author: last.commit.author.name,
    };
  } catch {
    return null;
  }
}

// ── Helpers ───────────────────────────────────────────────────────────────────

function daysSince(isoDate) {
  return Math.floor((Date.now() - new Date(isoDate).getTime()) / 86400000);
}

function isWIPTitle(title) {
  return /\b(WIP|DO NOT (MERGE|REVIEW)|NOT READY)\b/i.test(title);
}

function categorize(pr) {
  if (pr.isDraft) return 'draft';
  if (isWIPTitle(pr.title)) return 'wip_not_draft';
  if (pr.ciStatus.overall === 'failing') return 'needs_attention';
  if (pr.reviewInfo.reviewDecision === 'changes_requested') return 'needs_attention';
  if (pr.daysSinceUpdate >= 3) return 'stale';
  if (pr.ciStatus.overall === 'passing' && ['approved', 'pending'].includes(pr.reviewInfo.reviewDecision)) return 'healthy';
  return 'in_progress';
}

// ── Context carryover ─────────────────────────────────────────────────────────

function getYesterdayReport(reportsDir) {
  try {
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    const dateStr = yesterday.toISOString().split('T')[0];
    const filepath = path.join(reportsDir, `pr-report-${dateStr}.md`);
    if (fs.existsSync(filepath)) {
      console.log(`Loading yesterday's report for context: ${filepath}`);
      return fs.readFileSync(filepath, 'utf8');
    }
  } catch { /* no-op */ }
  return null;
}

// ── Data collection ───────────────────────────────────────────────────────────

async function collectPRData() {
  const rawPRs = await getOpenPRs();
  const enriched = [];

  for (const pr of rawPRs) {
    process.stdout.write(`  #${pr.number} "${pr.title.substring(0, 40)}"... `);
    const [ciStatus, reviewInfo, latestCommit] = await Promise.all([
      getCIStatus(pr.head.sha),
      getReviewInfo(pr.number),
      getLatestCommit(pr.number),
    ]);

    const enrichedPR = {
      number: pr.number,
      title: pr.title,
      url: `${REPO_URL}/pull/${pr.number}`,
      author: pr.user.login,
      branch: pr.head.ref,
      targetBranch: pr.base.ref,
      createdAt: pr.created_at,
      updatedAt: pr.updated_at,
      ageInDays: daysSince(pr.created_at),
      daysSinceUpdate: daysSince(pr.updated_at),
      isDraft: pr.draft,
      labels: pr.labels.map(l => l.name),
      requestedReviewers: pr.requested_reviewers.map(r => r.login),
      requestedTeams: (pr.requested_teams || []).map(t => t.name),
      additions: pr.additions,
      deletions: pr.deletions,
      changedFiles: pr.changed_files,
      ciStatus,
      reviewInfo,
      latestCommit,
    };

    enrichedPR.category = categorize(enrichedPR);
    enriched.push(enrichedPR);
    console.log(`[${enrichedPR.category}]`);
  }

  return enriched;
}

// ── Claude report generation ──────────────────────────────────────────────────

async function generateReport(prData, yesterdayReport) {
  const today = new Date().toISOString().split('T')[0];

  const groups = {
    needs_attention: prData.filter(p => p.category === 'needs_attention'),
    stale:          prData.filter(p => p.category === 'stale'),
    wip_not_draft:  prData.filter(p => p.category === 'wip_not_draft'),
    healthy:        prData.filter(p => p.category === 'healthy'),
    in_progress:    prData.filter(p => p.category === 'in_progress'),
    draft:          prData.filter(p => p.category === 'draft'),
  };

  const yesterdaySection = yesterdayReport
    ? `## Yesterday's Report (context carryover)\n\n${yesterdayReport.substring(0, 3000)}\n\n---\n`
    : '(No previous report — this is day one.)';

  const prompt = `You are an automated daily PR reporter for the rocprofiler-systems subproject (label: ${PR_LABEL}) within the GitHub repository ${OWNER}/${REPO}.

Today's date: ${today}
Total open PRs: ${prData.length}

${yesterdaySection}

## Today's PR Data
${JSON.stringify(groups, null, 2)}

---

Generate a Markdown daily PR report following these rules exactly:

FORMATTING:
- Every PR MUST be hyperlinked: [${REPO}#123](${REPO_URL}/pull/123)
- Every author MUST be hyperlinked: [@user](https://github.com/user)
- Tables must have columns: PR | Title | Author | CI | Review Status | Last Updated | Age
- Emojis: ✅ passing ❌ failing ⏳ in_progress 📝 draft 🔄 changes_requested 🚨 urgent ⚠️ warning

STRUCTURE — use exactly these sections:

# rocprofiler-systems — Daily PR Report ${today}
> Filtered from [${OWNER}/${REPO}](${REPO_URL}) · label: \`${PR_LABEL}\`

## Executive Summary
2-3 sentences: total PRs, biggest risk today, CI health snapshot.
If yesterday's report exists: what got resolved, what's newly stuck, what changed.

## ⚠️ Needs Attention
(${groups.needs_attention.length} PRs) — Failing CI or changes requested. Table + note the specific failing checks or who requested changes.

## 🕰️ Stale (3+ days no activity)
(${groups.stale.length} PRs) — Table with days-since-update highlighted.

## ⚡ WIP / Not Marked as Draft
(${groups.wip_not_draft.length} PRs) — Titles suggest not ready but aren't drafts. Flag for conversion.

## ✅ Healthy
(${groups.healthy.length} PRs) — Passing CI, approved or awaiting review. Table.

## ⏳ In Progress
(${groups.in_progress.length} PRs) — Active work, CI running. Brief table.

## 📝 Drafts
(${groups.draft.length} PRs) — Brief list only, no table needed.

## CI Health Snapshot
One paragraph: X/total passing, X failing, X in progress, X no checks.
List names of failing checks if any.

## What Changed Since Yesterday
(Only if yesterday's report provided) Bullet list:
- Newly opened PRs
- PRs that got merged/closed
- CI status changes (pass→fail or fail→pass)
- PRs that received reviews
- PRs that became stale

## Recommended Actions
Numbered, ordered by priority. Be specific — name the PR and what needs to happen.

---
*Auto-generated: ${today}*`;

  console.log('Generating report with Claude...');
  const message = await anthropic.messages.create({
    model: 'claude-sonnet-4-20250514',
    max_tokens: 4096,
    messages: [{ role: 'user', content: prompt }],
  });

  return message.content[0].text;
}

// ── Entry point ───────────────────────────────────────────────────────────────

async function main() {
  try {
    const reportsDir = path.join(process.cwd(), 'reports');
    if (!fs.existsSync(reportsDir)) fs.mkdirSync(reportsDir, { recursive: true });

    const yesterdayReport = getYesterdayReport(reportsDir);
    const prData = await collectPRData();
    const report = await generateReport(prData, yesterdayReport);

    const today = new Date().toISOString().split('T')[0];
    const datedFile = path.join(reportsDir, `pr-report-${today}.md`);
    const latestFile = path.join(reportsDir, 'pr-report-latest.md');

    fs.writeFileSync(datedFile, report);
    fs.writeFileSync(latestFile, report);

    console.log(`\n✅ Saved: ${datedFile}`);
    console.log(`✅ Latest: ${latestFile}`);
  } catch (err) {
    console.error('Fatal:', err);
    process.exit(1);
  }
}

main();
