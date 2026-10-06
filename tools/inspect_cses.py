import re
import pathlib

p = pathlib.Path(r"C:\Users\raviranjan\.gemini\antigravity-ide\brain\f36a46b0-9125-4abb-8386-6513a48c849e\.system_generated\steps\372\content.md")
text = p.read_text(encoding="utf-8")
sections = re.findall(r"<h2>(.*?)</h2>(.*?)(?=<h2>|$)", text, re.DOTALL)
for s_name, s_html in sections:
    tasks = re.findall(r'task/\d+">([^<]+)</a>', s_html)
    print(f"=== {s_name} ({len(tasks)}) ===")
    for t in tasks:
        print(f"  - {t}")

