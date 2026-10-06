import os
import re
from pathlib import Path

cdir = Path('00-Start-Here/concepts')

for fname in ['01-getting-started-basics.md', '03-cpp-fundamentals.md', '07-conditionals-and-loops.md', '09-pointers-and-memory-model.md', '10-arrays-and-vectors-intro.md']:
    fp = cdir / fname
    text = fp.read_text(encoding='utf-8')
    lines = text.splitlines()
    print(f"=== {fname} ({len(lines)} lines) ===")
    h1_and_h2 = [l.strip() for l in lines if l.startswith('# ') or l.startswith('## ')]
    for h in h1_and_h2[:12]:
        # print safe ascii
        safe_h = h.encode('ascii', errors='replace').decode('ascii')
        print(f"  {safe_h}")
    print(f"  Total sections: {len(h1_and_h2)}")
