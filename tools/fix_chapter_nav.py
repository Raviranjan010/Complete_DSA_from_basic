#!/usr/bin/env python3
"""
Fixes chapter navigation headers in 00-Start-Here/concepts/ to link to the exact filenames.
"""

from pathlib import Path

cdir = Path('00-Start-Here/concepts')

groups = [
    '01-getting-started-basics',
    '03-cpp-fundamentals',
    '07-conditionals-and-loops',
    '09-pointers-and-memory-model',
    '10-arrays-and-vectors-intro'
]

for g in groups:
    chaps = sorted([f for f in cdir.iterdir() if f.name.startswith(f"{g}-ch")])
    index_file = f"{g}.md"
    for i, ch_path in enumerate(chaps):
        text = ch_path.read_text(encoding='utf-8')
        lines = text.splitlines()

        # Build clean navigation
        prev_link = f"[← Chapter {i:02d}]({chaps[i-1].name}) · " if i > 0 else ""
        next_link = f" · [Chapter {i+2:02d} →]({chaps[i+1].name})" if i < len(chaps) - 1 else ""
        nav_line = f"{prev_link}[Chapter Index]({index_file}) · [Module Overview](../README.md){next_link}"

        # Replace first lines up to ---
        if '---' in lines[:6]:
            sep_idx = lines[:6].index('---')
            new_lines = [nav_line, "", "---"] + lines[sep_idx+1:]
        else:
            new_lines = [nav_line, "", "---"] + lines

        ch_path.write_text('\n'.join(new_lines).strip() + '\n', encoding='utf-8')

print("Fixed chapter navigation links.")
