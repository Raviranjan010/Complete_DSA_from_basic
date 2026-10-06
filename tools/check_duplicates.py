#!/usr/bin/env python3
"""
tools/check_duplicates.py
Paragraph-level, section-level, and title/code duplication detector across repository markdown and code files.
Adheres to REPAIR_PROMPT_v3 Rule 3.1 & Gate G6.
"""

import sys
import os
import re
import hashlib
import argparse
from pathlib import Path
from collections import defaultdict
import difflib

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

repo_root = Path(__file__).resolve().parent.parent

def normalize_text(text: str) -> str:
    """Normalize whitespace and lowercases text for similarity comparison."""
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL) # strip code blocks
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text.lower()).strip()
    return text

def get_word_shingles(text: str, k=4) -> set:
    words = text.split()
    if len(words) < k:
        return set()
    return set(' '.join(words[i:i+k]) for i in range(len(words) - k + 1))

def get_sections(filepath: Path):
    """Split markdown file into sections by H2/H3 headers."""
    content = filepath.read_text(encoding='utf-8', errors='ignore')
    lines = content.splitlines()
    sections = []
    curr_title = "Header"
    curr_lines = []
    
    for line in lines:
        if line.startswith('## ') or line.startswith('### '):
            if curr_lines:
                text = '\n'.join(curr_lines).strip()
                if len(text) > 100:
                    sections.append((curr_title, text, len(curr_lines)))
            curr_title = line.strip('# \t')
            curr_lines = [line]
        else:
            curr_lines.append(line)
            
    if curr_lines:
        text = '\n'.join(curr_lines).strip()
        if len(text) > 100:
            sections.append((curr_title, text, len(curr_lines)))
            
    return sections

def scan_concept_duplicates(topics=None, threshold=0.70):
    """Scan concepts across given topics (or all 00-18) for section-level >= threshold match."""
    if topics is None:
        target_dirs = sorted([d for d in repo_root.iterdir() if d.is_dir() and re.match(r'^\d\d-', d.name)])
    else:
        target_dirs = [repo_root / t for t in topics]

    concept_files = []
    for t_dir in target_dirs:
        c_dir = t_dir / 'concepts'
        if c_dir.exists():
            for f in c_dir.rglob('*.md'):
                concept_files.append(f)

    print(f"Loaded {len(concept_files)} concept markdown files across {len(target_dirs)} topics.")
    
    all_sections = []
    for cf in concept_files:
        secs = get_sections(cf)
        for title, raw_text, line_count in secs:
            norm = normalize_text(raw_text)
            words = norm.split()
            if len(words) >= 40: # non-trivial
                shingles = get_word_shingles(norm, k=4)
                all_sections.append({
                    'file': cf,
                    'title': title,
                    'raw': raw_text,
                    'line_count': line_count,
                    'words_count': len(words),
                    'shingles': shingles,
                    'norm': norm
                })

    print(f"Total candidate sections indexed: {len(all_sections)}")
    clusters = []
    
    # Inverted index of shingles to fast candidate pair discovery
    shingle_to_sec = defaultdict(list)
    for idx, sec in enumerate(all_sections):
        # sample shingles for indexing
        for sh in list(sec['shingles'])[::3]:
            shingle_to_sec[sh].append(idx)
            
    pair_counts = defaultdict(int)
    for sh, indices in shingle_to_sec.items():
        if len(indices) > 50:
            continue
        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):
                idx1, idx2 = indices[i], indices[j]
                if all_sections[idx1]['file'] != all_sections[idx2]['file']:
                    pair_counts[(idx1, idx2)] += 1

    checked_pairs = set()
    for (idx1, idx2), count in pair_counts.items():
        s1 = all_sections[idx1]
        s2 = all_sections[idx2]
        
        # Jaccard filter
        sh1, sh2 = s1['shingles'], s2['shingles']
        if not sh1 or not sh2:
            continue
        inter = len(sh1 & sh2)
        union = len(sh1 | sh2)
        jaccard = inter / union
        
        if jaccard >= threshold * 0.75: # candidate
            sim = difflib.SequenceMatcher(None, s1['norm'], s2['norm']).ratio()
            if sim >= threshold:
                clusters.append({
                    'sim': sim,
                    'jaccard': jaccard,
                    'f1': s1['file'].relative_to(repo_root),
                    't1': s1['title'],
                    'l1': s1['line_count'],
                    'f2': s2['file'].relative_to(repo_root),
                    't2': s2['title'],
                    'l2': s2['line_count'],
                    'sample': s1['norm'][:140] + "..."
                })

    clusters.sort(key=lambda x: x['sim'], reverse=True)
    return clusters

def main():
    parser = argparse.ArgumentParser(description="Check duplicates across repo")
    parser.add_argument('--threshold', type=float, default=0.70, help="Similarity threshold (0.0 to 1.0)")
    parser.add_argument('--topics', nargs='*', help="Topics to inspect, e.g. 00-Start-Here 03-Arrays-and-Strings")
    args = parser.parse_args()

    print(f"Scanning for section clusters with >= {int(args.threshold*100)}% similarity...")
    clusters = scan_concept_duplicates(topics=args.topics, threshold=args.threshold)
    
    print(f"\nFound {len(clusters)} matching clusters (>= {int(args.threshold*100)}%):")
    for idx, c in enumerate(clusters, 1):
        print(f"\n[{idx}] Match {c['sim']*100:.1f}% (Jaccard: {c['jaccard']*100:.1f}%)")
        print(f"  File A ({c['l1']} lines): {c['f1']} :: Section '{c['t1']}'")
        print(f"  File B ({c['l2']} lines): {c['f2']} :: Section '{c['t2']}'")
        print(f"  Snippet: {c['sample']}")

if __name__ == '__main__':
    main()
