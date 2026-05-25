#!/usr/bin/env python3
"""Convert a markdown report to a styled HTML page for GitHub Pages."""

import os
import re
import sys
import html


def md_to_html(md_text):
    """Lightweight markdown-to-HTML converter (no external dependencies)."""
    lines = md_text.split("\n")
    out = []
    in_table = False
    in_code = False
    in_list = False
    in_blockquote = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            if in_code:
                out.append("</code></pre>")
                in_code = False
            else:
                lang = stripped[3:].strip()
                out.append(f'<pre><code class="{html.escape(lang)}">')
                in_code = True
            continue

        if in_code:
            out.append(html.escape(line))
            continue

        if not stripped:
            if in_list:
                out.append("</ul>")
                in_list = False
            if in_blockquote:
                out.append("</blockquote>")
                in_blockquote = False
            if in_table:
                out.append("</tbody></table>")
                in_table = False
            out.append("")
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if all(re.match(r"^[-:]+$", c) for c in cells):
                continue
            if not in_table:
                out.append('<table><thead>')
                out.append("<tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells) + "</tr>")
                out.append("</thead><tbody>")
                in_table = True
            else:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells) + "</tr>")
            continue

        if in_table and not stripped.startswith("|"):
            out.append("</tbody></table>")
            in_table = False

        if stripped.startswith("> "):
            if not in_blockquote:
                out.append("<blockquote>")
                in_blockquote = True
            out.append(f"<p>{inline(stripped[2:])}</p>")
            continue

        if in_blockquote and not stripped.startswith(">"):
            out.append("</blockquote>")
            in_blockquote = False

        if stripped.startswith("- "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(stripped[2:])}</li>")
            continue

        if re.match(r"^\d+\.\s", stripped):
            content = re.sub(r"^\d+\.\s", "", stripped)
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(content)}</li>")
            continue

        if in_list:
            out.append("</ul>")
            in_list = False

        if stripped.startswith("---"):
            out.append("<hr>")
            continue

        m = re.match(r"^(#{1,6})\s+(.*)", stripped)
        if m:
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            continue

        out.append(f"<p>{inline(stripped)}</p>")

    if in_list:
        out.append("</ul>")
    if in_blockquote:
        out.append("</blockquote>")
    if in_table:
        out.append("</tbody></table>")
    if in_code:
        out.append("</code></pre>")

    return "\n".join(out)


def inline(text):
    """Process inline markdown: bold, italic, code, links, emoji."""
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        r'<a href="\2" target="_blank">\1</a>',
        text,
    )
    return text


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  :root {{
    --bg: #0d1117;
    --fg: #e6edf3;
    --muted: #8b949e;
    --accent: #58a6ff;
    --border: #30363d;
    --card: #161b22;
    --green: #3fb950;
    --red: #f85149;
    --yellow: #d29922;
    --orange: #db6d28;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    background: var(--bg);
    color: var(--fg);
    line-height: 1.7;
    padding: 2rem;
    max-width: 1100px;
    margin: 0 auto;
  }}
  h1 {{ font-size: 1.8rem; margin: 1.5rem 0 0.5rem; border-bottom: 1px solid var(--border); padding-bottom: 0.4rem; }}
  h2 {{ font-size: 1.4rem; margin: 1.8rem 0 0.6rem; color: var(--accent); }}
  h3 {{ font-size: 1.15rem; margin: 1.2rem 0 0.4rem; color: var(--muted); }}
  p {{ margin: 0.5rem 0; }}
  a {{ color: var(--accent); text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  code {{
    background: var(--card);
    padding: 0.15em 0.4em;
    border-radius: 4px;
    font-size: 0.9em;
    font-family: 'SFMono-Regular', Consolas, monospace;
  }}
  pre {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1rem;
    overflow-x: auto;
    margin: 0.8rem 0;
  }}
  pre code {{
    background: none;
    padding: 0;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 0.8rem 0;
    font-size: 0.9rem;
  }}
  th, td {{
    padding: 0.5rem 0.75rem;
    border: 1px solid var(--border);
    text-align: left;
  }}
  th {{
    background: var(--card);
    font-weight: 600;
    color: var(--accent);
    position: sticky;
    top: 0;
  }}
  tr:nth-child(even) {{ background: rgba(22,27,34,0.5); }}
  tr:hover {{ background: rgba(88,166,255,0.08); }}
  ul {{ margin: 0.5rem 0 0.5rem 1.5rem; }}
  li {{ margin: 0.3rem 0; }}
  blockquote {{
    border-left: 3px solid var(--yellow);
    padding: 0.5rem 1rem;
    margin: 0.8rem 0;
    background: rgba(210,153,34,0.06);
    border-radius: 0 6px 6px 0;
  }}
  hr {{
    border: none;
    border-top: 1px solid var(--border);
    margin: 1.5rem 0;
  }}
  strong {{ color: #f0f6fc; }}
  .timestamp {{
    color: var(--muted);
    font-size: 0.85rem;
    text-align: center;
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 1px solid var(--border);
  }}
</style>
</head>
<body>
{body}
</body>
</html>"""


def convert_file(md_path, html_path):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    title_match = re.search(r"^#\s+(.+)", md_text, re.MULTILINE)
    title = title_match.group(1) if title_match else "Daily PR Report"

    body_html = md_to_html(md_text)
    full_html = HTML_TEMPLATE.format(title=html.escape(title), body=body_html)

    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Converted: {md_path} -> {html_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <input.md> <output.html>")
        sys.exit(1)
    convert_file(sys.argv[1], sys.argv[2])
