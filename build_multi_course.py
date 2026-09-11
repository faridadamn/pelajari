# -*- coding: utf-8 -*-
"""
Multi-Course Compiler for Pelajari OS
Compiles both masterclasses:
1. Caleb Ralston Masterclass OS (7 Tracks, 42 items)
2. Alex Hormozi Business OS ($100M Architecture) (8 Tracks, 48 items)
Outputs:
- /root/pelajari/courses_data.json
- /root/pelajari/modules_data.json (default Caleb for backward compatibility)
"""

import os, sys, re, json, html, glob

OUT_DIR = "/root/pelajari"
os.makedirs(OUT_DIR, exist_ok=True)

# ------------------------------------------------------------------------------
# LATEX & SPECIAL CHARACTER SANITIZER
# ------------------------------------------------------------------------------
def sanitize_latex(text):
    # LaTeX Arrow Replacements
    text = re.sub(r"\$\s*\\?n?r?ightarrow\s*\$", "→", text)
    text = re.sub(r"\\?n?r?ightarrow", "→", text)
    text = re.sub(r"\$\s*\\?longrightarrow\s*\$", "→", text)
    text = re.sub(r"\\?longrightarrow", "→", text)
    text = re.sub(r"\$\s*\\?leftarrow\s*\$", "←", text)
    text = re.sub(r"\\?leftarrow", "←", text)
    text = re.sub(r"\$\s*\\?leftrightarrow\s*\$", "↔", text)
    text = re.sub(r"\\?leftrightarrow", "↔", text)
    
    # Operators & Symbols
    text = re.sub(r"\\times", "×", text)
    text = re.sub(r"\$\s*\\times\s*\$", "×", text)
    text = re.sub(r"\\approx", "≈", text)
    text = re.sub(r"\$\s*\\approx\s*\$", "≈", text)
    
    # Formatting commands
    text = re.sub(r"\\text\{([^}]+)\}", r"\1", text)
    text = re.sub(r"\\textbf\{([^}]+)\}", r"<strong>\1</strong>", text)
    text = re.sub(r"\\frac\{([^}]+)\}\{([^}]+)\}", r"(\1 / \2)", text)
    
    # Strip unnecessary math markers
    text = re.sub(r"\$\$([^$]+)\$\$", r"\1", text)
    text = re.sub(r"\$([^$\n]+)\$", r"\1", text)
    
    return text

# ------------------------------------------------------------------------------
# MARKDOWN RENDERER
# ------------------------------------------------------------------------------
def format_inline(text):
    text = sanitize_latex(text)
    text = html.escape(text)
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", text)
    text = re.sub(r"`(.*?)`", r"<code>\1</code>", text)
    text = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    return text

def render_markdown(md_text):
    lines = md_text.split('\n')
    out = []
    in_code = False
    in_table = False
    in_list = False
    code_lines = []
    table_lines = []
    
    for line in lines:
        raw = line
        stripped = line.strip()
        
        if stripped.startswith("```"):
            if in_code:
                in_code = False
                code_content = html.escape("\n".join(code_lines))
                out.append(f'<div class="code-wrap"><div class="code-header"><span class="code-tag">DIAGRAM / FORMULA</span><button class="btn-copy-code" onclick="copySnippet(this)">Salin Diagram</button></div><pre><code>{code_content}</code></pre></div>')
                code_lines = []
            else:
                in_code = True
                code_lines = []
            continue
        
        if in_code:
            code_lines.append(raw)
            continue
            
        if stripped.startswith("|") and stripped.endswith("|"):
            if not in_table:
                in_table = True
                table_lines = [stripped]
            else:
                table_lines.append(stripped)
            continue
        else:
            if in_table:
                in_table = False
                t_html = ['<div class="table-wrap"><table>']
                is_head = True
                for t_row in table_lines:
                    if re.match(r"^\|[\s\-:]+(\|[\s\-:]+)+\|$", t_row):
                        is_head = False
                        continue
                    cells = [c.strip() for c in t_row.split("|")[1:-1]]
                    t_html.append('<tr>')
                    tag = "th" if is_head else "td"
                    for cell in cells:
                        cell_fmt = format_inline(cell)
                        t_html.append(f'<{tag}>{cell_fmt}</{tag}>')
                    t_html.append('</tr>')
                t_html.append('</table></div>')
                out.append("\n".join(t_html))
                table_lines = []
                
        if stripped.startswith("- ") or stripped.startswith("* "):
            if not in_list:
                in_list = True
                out.append('<ul>')
            item_text = format_inline(stripped[2:])
            out.append(f'<li>{item_text}</li>')
            continue
        elif re.match(r"^\d+\.\s+", stripped):
            if not in_list:
                in_list = True
                out.append('<ol>')
            item_text = format_inline(re.sub(r"^\d+\.\s+", "", stripped))
            out.append(f'<li>{item_text}</li>')
            continue
        else:
            if in_list:
                in_list = False
                out.append('</ul>' if out[-1].startswith('<li>') else '</ol>')
                
        if not stripped:
            continue
            
        if stripped.startswith("# "):
            out.append(f'<h1 class="mod-title">{format_inline(stripped[2:])}</h1>')
        elif stripped.startswith("## "):
            out.append(f'<h2 class="mod-sub">{format_inline(stripped[3:])}</h2>')
        elif stripped.startswith("### "):
            layer_id = ""
            h3_text = stripped[4:].strip()
            if "LAYER 1" in h3_text.upper():
                layer_id = ' id="layer-1" data-layer="1"'
            elif "LAYER 2" in h3_text.upper():
                layer_id = ' id="layer-2" data-layer="2"'
            elif "LAYER 3" in h3_text.upper():
                layer_id = ' id="layer-3" data-layer="3"'
            elif "LAYER 4" in h3_text.upper():
                layer_id = ' id="layer-4" data-layer="4"'
            elif "LAYER 5" in h3_text.upper():
                layer_id = ' id="layer-5" data-layer="5"'
            out.append(f'<h3 class="layer-header"{layer_id}>{format_inline(h3_text)}</h3>')
        elif stripped.startswith("#### "):
            out.append(f'<h4 class="sub-header">{format_inline(stripped[5:])}</h4>')
        elif stripped.startswith("> "):
            out.append(f'<blockquote class="quote-box">{format_inline(stripped[2:])}</blockquote>')
        elif stripped == "---":
            out.append('<hr class="divider" />')
        else:
            out.append(f'<p class="prose">{format_inline(stripped)}</p>')
            
    if in_code:
        code_content = html.escape("\n".join(code_lines))
        out.append(f'<pre><code>{code_content}</code></pre>')
    if in_table:
        out.append('</table></div>')
    if in_list:
        out.append('</ul>')
        
    return "\n".join(out)

def discover_course_tracks(base_dir, prefix):
    track_dirs = sorted([d for d in glob.glob(os.path.join(base_dir, 'track_*')) if os.path.isdir(d)])
    items = []
    
    for tdir in track_dirs:
        tname = os.path.basename(tdir)
        t_num = re.search(r'track_(\d+)', tname).group(1)
        
        # Read README.md
        readme_path = os.path.join(tdir, 'README.md')
        track_title = f'Track {t_num}'
        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding='utf-8') as f:
                r_first = f.readline().strip()
                m_title = re.search(r'TRACK \d+:\s*(.*?)$', r_first, re.IGNORECASE)
                if m_title:
                    track_title = f'Track {t_num}: {m_title.group(1).title()}'
            
            with open(readme_path, 'r', encoding='utf-8') as f:
                raw_md = f.read()
            
            items.append({
                'id': f'overview_{prefix}{t_num}',
                'track': f'track{t_num}',
                'track_title': track_title,
                'title': f'Peta Kurikulum Track {t_num}',
                'badge': f'Track {t_num}',
                'duration': '5 menit',
                'file': readme_path,
                'raw_md': raw_md,
                'worksheet': '',
                'html': render_markdown(raw_md)
            })
            
        # Discover M*.md files
        mfiles = sorted(glob.glob(os.path.join(tdir, 'M*.md')))
        for mf in mfiles:
            fname = os.path.basename(mf)
            m_num = re.search(r'M(\d+)', fname).group(1)
            with open(mf, 'r', encoding='utf-8') as f:
                raw_md = f.read()
            m_h2 = re.search(r'^## (Modul \d+:\s*(.*?))$', raw_md, re.MULTILINE)
            if m_h2:
                m_title = m_h2.group(1).strip()
            else:
                m_title = f'Modul {m_num}'
                
            worksheet_match = re.search(r"### LAYER 4:.*?\n(.*?)(?=\n### LAYER 5|\Z)", raw_md, re.DOTALL)
            worksheet_text = worksheet_match.group(1).strip() if worksheet_match else ""
            
            items.append({
                'id': f'{prefix}m{m_num}',
                'track': f'track{t_num}',
                'track_title': track_title,
                'title': m_title,
                'badge': f'Modul {m_num}',
                'duration': '15 menit',
                'file': mf,
                'raw_md': raw_md,
                'worksheet': worksheet_text,
                'html': render_markdown(raw_md)
            })
            
    return items

def main():
    print("Auto-discovering & compiling Caleb Ralston Masterclass OS...")
    caleb_modules = discover_course_tracks('/root/caleb_masterclass', '')
    print(f"Caleb items compiled: {len(caleb_modules)}")

    print("Auto-discovering & compiling Alex Hormozi Business OS...")
    hormozi_modules = discover_course_tracks('/root/hormozi_masterclass', 'h')
    print(f"Hormozi items compiled: {len(hormozi_modules)}")

    print("Auto-discovering & compiling Career Contessa Workplace OS...")
    careercontessa_modules = discover_course_tracks('/root/careercontessa_masterclass', 'cc')
    print(f"Career Contessa items compiled: {len(careercontessa_modules)}")

    print("Auto-discovering & compiling Wes Roth AI Intelligence OS...")
    wesroth_modules = discover_course_tracks('/root/wesroth_masterclass', 'wr')
    print(f"Wes Roth items compiled: {len(wesroth_modules)}")

    courses_data = {
        "caleb": {
            "id": "caleb",
            "title": "Caleb Ralston Masterclass OS",
            "short_title": "Caleb Ralston OS",
            "subtitle": "The Zero-to-One Million Audience Engine & Personal Brand Architecture",
            "author": "Caleb Ralston",
            "tracks_count": 7,
            "modules_count": 35,
            "total_items": len(caleb_modules),
            "modules": caleb_modules
        },
        "hormozi": {
            "id": "hormozi",
            "title": "Alex Hormozi Business OS",
            "short_title": "Alex Hormozi $100M",
            "subtitle": "The $100M Acquisition, Offer & Enterprise Scaling Architecture",
            "author": "Alex Hormozi",
            "tracks_count": 8,
            "modules_count": 40,
            "total_items": len(hormozi_modules),
            "modules": hormozi_modules
        },
        "careercontessa": {
            "id": "careercontessa",
            "title": "Career Contessa Workplace OS",
            "short_title": "Career Contessa OS",
            "subtitle": "The Career & Workplace Acceleration OS (Interviews, Salary, Politics & Leadership)",
            "author": "Career Contessa & Lauren McGoodwin",
            "tracks_count": 8,
            "modules_count": 40,
            "total_items": len(careercontessa_modules),
            "modules": careercontessa_modules
        },
        "wesroth": {
            "id": "wesroth",
            "title": "Wes Roth AI Intelligence OS",
            "short_title": "Wes Roth AI OS",
            "subtitle": "The AI Frontier, Reasoning, Autonomous Systems & Hardware Economics OS",
            "author": "Wes Roth",
            "tracks_count": 8,
            "modules_count": 40,
            "total_items": len(wesroth_modules),
            "modules": wesroth_modules
        }
    }

    # Write courses_data.json
    courses_json_path = os.path.join(OUT_DIR, "courses_data.json")
    with open(courses_json_path, "w", encoding="utf-8") as f:
        json.dump(courses_data, f)
    print(f"Saved {courses_json_path} ({os.path.getsize(courses_json_path)} bytes).")

    # Write legacy modules_data.json
    legacy_json_path = os.path.join(OUT_DIR, "modules_data.json")
    with open(legacy_json_path, "w", encoding="utf-8") as f:
        json.dump(caleb_modules, f)
    print(f"Saved legacy {legacy_json_path} ({os.path.getsize(legacy_json_path)} bytes).")

if __name__ == "__main__":
    main()
