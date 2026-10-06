import os
from pathlib import Path
from collections import Counter

cdir = Path('00-Start-Here/concepts')

for fname in ['01-getting-started-basics.md', '03-cpp-fundamentals.md', '07-conditionals-and-loops.md', '09-pointers-and-memory-model.md', '10-arrays-and-vectors-intro.md']:
    fp = cdir / fname
    text = fp.read_text(encoding='utf-8')
    lines = [l.strip() for l in text.splitlines() if len(l.strip()) > 30 and not l.strip().startswith('```')]
    counts = Counter(lines)
    dups = [(l, c) for l, c in counts.items() if c > 1]
    print(f"{fname}: {len(lines)} substantive lines, {len(dups)} duplicated lines (repeated {sum(c for _, c in dups) - len(dups)} times)")
