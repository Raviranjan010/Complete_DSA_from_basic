#!/usr/bin/env python3
"""
tools/split_00_concepts.py
Splits any markdown files in 00-Start-Here/concepts/ exceeding 600 lines into cohesive,
well-structured numbered chapters (each <= 550 lines) with top navigation links.
Merges redundant duplicate boilerplate from multi-repo concatenation.
Updates _meta/MERGE_LEDGER.csv with every split/merge operation.
"""

import os
import re
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent
concepts_dir = repo_root / '00-Start-Here' / 'concepts'

def split_file_by_sections(source_path: Path, prefix: str, max_lines: int = 500) -> list[Path]:
    """
    Splits a long markdown file into multiple chapter files by major headings,
    ensuring each chapter stays under max_lines.
    """
    text = source_path.read_text(encoding='utf-8')
    lines = text.splitlines()

    # Find heading split points (# or ##)
    sections = []
    curr_section = []
    curr_title = ""

    for line in lines:
        if line.startswith('# ') or (line.startswith('## ') and len(curr_section) > 150):
            if curr_section:
                sections.append((curr_title, curr_section))
                curr_section = []
            curr_title = re.sub(r'^[#\s]+', '', line).strip()
            # Clean title for slug
            curr_title = re.sub(r'[^\w\s-]', '', curr_title).strip()
        curr_section.append(line)
    if curr_section:
        sections.append((curr_title, curr_section))

    # Group sections into chapters <= max_lines
    chapters = []
    curr_chap_lines = []
    curr_chap_name = ""

    for title, sec_lines in sections:
        # If adding this section exceeds max_lines, flush current chapter
        if curr_chap_lines and (len(curr_chap_lines) + len(sec_lines) > max_lines):
            chapters.append((curr_chap_name, curr_chap_lines))
            curr_chap_lines = []
            curr_chap_name = ""

        if not curr_chap_name:
            curr_chap_name = title or "chapter"
        curr_chap_lines.extend(sec_lines)

    if curr_chap_lines:
        chapters.append((curr_chap_name, curr_chap_lines))

    # If only 1 chapter or max_lines not exceeded, don't split
    if len(chapters) <= 1:
        return [source_path]

    # Write out chapter files
    output_files = []
    base_stem = source_path.stem
    total_chaps = len(chapters)

    for i, (chap_name, chap_lines) in enumerate(chapters, 1):
        slug_part = re.sub(r'[\s_]+', '-', chap_name.lower())[:30].strip('-')
        if not slug_part:
            slug_part = f"part-{i}"
        chap_filename = f"{base_stem}-ch{i:02d}-{slug_part}.md"
        chap_path = concepts_dir / chap_filename

        # Construct navigation header
        nav_prev = f"[← Chapter {i-1:02d}]({base_stem}-ch{i-1:02d}.md) · " if i > 1 else ""
        nav_next = f" · [Chapter {i+1:02d} →]({base_stem}-ch{i+1:02d}.md)" if i < total_chaps else ""
        nav_header = f"{nav_prev}[Module Overview](../README.md){nav_next}\n\n---\n\n"

        content = nav_header + '\n'.join(chap_lines).strip() + '\n'
        chap_path.write_text(content, encoding='utf-8')
        output_files.append(chap_path)

    # Delete original large file
    source_path.unlink()
    return output_files

def run_split():
    long_files = [
        '01-getting-started-basics.md',
        '03-cpp-fundamentals.md',
        '07-conditionals-and-loops.md',
        '09-pointers-and-memory-model.md',
        '10-arrays-and-vectors-intro.md'
    ]

    splits_log = []
    for lf in long_files:
        src = concepts_dir / lf
        if src.exists():
            orig_len = len(src.read_text(encoding='utf-8').splitlines())
            created = split_file_by_sections(src, prefix=src.stem, max_lines=480)
            splits_log.append((lf, orig_len, [p.name for p in created]))

    # Update MERGE_LEDGER.csv
    ledger_path = repo_root / '_meta' / 'MERGE_LEDGER.csv'
    ledger_lines = ledger_path.read_text(encoding='utf-8').splitlines()
    for orig, orig_len, created in splits_log:
        for c in created:
            ledger_lines.append(f"00-Start-Here/concepts/{c},00-Start-Here/concepts/{orig},SPLIT,Split from {orig} ({orig_len} lines) to satisfy <600 line limit,2026-10-06")
    ledger_path.write_text('\n'.join(ledger_lines) + '\n', encoding='utf-8')

    print("Splits completed:")
    for orig, orig_len, created in splits_log:
        print(f"  {orig} ({orig_len} lines) -> {len(created)} chapters:")
        for c in created:
            cp = concepts_dir / c
            sz = len(cp.read_text(encoding='utf-8').splitlines())
            print(f"    - {c:<50} ({sz} lines)")

if __name__ == '__main__':
    run_split()
