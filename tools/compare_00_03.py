import sys
from pathlib import Path
import re, difflib
from collections import defaultdict

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

f00 = sorted(Path('00-Start-Here/concepts').glob('10-arrays*ch*'))
f03 = sorted(Path('03-Arrays-and-Strings/concepts').glob('*.md'))

def get_word_shingles(text, k=4):
    words = re.findall(r'[a-zA-Z0-9]+', text.lower())
    if len(words) < k:
        return set()
    return set(' '.join(words[i:i+k]) for i in range(len(words)-k+1))

def extract_sections(f):
    lines = f.read_text(encoding='utf-8', errors='ignore').splitlines()
    secs = []
    curr_t, curr_l = 'Intro', []
    for l in lines:
        if l.startswith('## ') or l.startswith('### '):
            if curr_l:
                text = '\n'.join(curr_l)
                if len(text) > 100:
                    secs.append((curr_t, text, len(curr_l)))
            curr_t, curr_l = l.strip('# \t'), [l]
        else:
            curr_l.append(l)
    if curr_l:
        text = '\n'.join(curr_l)
        if len(text) > 100:
            secs.append((curr_t, text, len(curr_l)))
    return secs

s00 = []
for p in f00:
    for t, txt, l in extract_sections(p):
        sh = get_word_shingles(txt)
        if len(sh) >= 20:
            s00.append((p.name, t, txt, l, sh))

s03 = []
for p in f03:
    for t, txt, l in extract_sections(p):
        sh = get_word_shingles(txt)
        if len(sh) >= 20:
            s03.append((p.name, t, txt, l, sh))

print(f"Indexed {len(s00)} sections in 00-Start-Here arrays, {len(s03)} sections in 03-Arrays-and-Strings.")

matches = []
for f00_name, t00, txt00, l00, sh00 in s00:
    for f03_name, t03, txt03, l03, sh03 in s03:
        inter = len(sh00 & sh03)
        if not inter: continue
        union = len(sh00 | sh03)
        jaccard = inter / union
        if jaccard >= 0.35: # potential cluster
            norm0 = re.sub(r'\s+', ' ', txt00.lower())
            norm3 = re.sub(r'\s+', ' ', txt03.lower())
            sim = difflib.SequenceMatcher(None, norm0, norm3).ratio()
            if sim >= 0.60:
                matches.append((sim, jaccard, f00_name, t00, l00, f03_name, t03, l03))

matches.sort(key=lambda x: x[0], reverse=True)
print(f"Found {len(matches)} matching section pairs (>= 60%):")
for m in matches:
    print(f"  {m[0]*100:.1f}% (Jaccard {m[1]*100:.1f}%) | 00: {m[2]} [{m[3]}] ({m[4]} lines) <===> 03: {m[5]} [{m[6]}] ({m[7]} lines)")
