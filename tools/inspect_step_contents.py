import os
from pathlib import Path

brain_step_dir = Path(r"C:\Users\raviranjan\.gemini\antigravity-ide\brain\f36a46b0-9125-4abb-8386-6513a48c849e\.system_generated\steps")

for step, name in [('376', 'Blind 75'), ('380', 'NeetCode 150'), ('384', 'Top 150'), ('372', 'CSES')]:
    f = brain_step_dir / step / 'content.md'
    if f.exists():
        text = f.read_text(encoding='utf-8')
        lines = text.splitlines()
        print(f"=== {name} (Step {step}): {len(lines)} lines ===")
        for i, l in enumerate(lines[:30]):
            safe = l.encode('ascii', errors='replace').decode('ascii')
            print(f"  {safe}")
