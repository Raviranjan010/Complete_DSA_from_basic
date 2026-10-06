from pathlib import Path
import re

p = Path(r"C:\Users\raviranjan\.gemini\antigravity-ide\brain\f36a46b0-9125-4abb-8386-6513a48c849e\.system_generated\steps\372\content.md")
text = p.read_text(encoding='utf-8')
tasks = re.findall(r'task/\d+">([^<]+)</a>', text)
print(f"Total CSES tasks found: {len(tasks)}")
for t in tasks[:15]:
    print(" ", t)
