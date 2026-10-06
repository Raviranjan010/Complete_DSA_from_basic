import os
import re
from pathlib import Path

ext_links = []
url_pattern = re.compile(r'https?://[^\s)\]"\'<>]+')

for root, dirs, files in os.walk('.'):
    # Exclude git, archive, and target directories
    parts = Path(root).parts
    if '.git' in parts or '_archive' in parts or 'target' in parts:
        continue
    for f in files:
        if f.endswith('.md'):
            fp = os.path.join(root, f)
            try:
                with open(fp, 'r', encoding='utf-8', errors='ignore') as mf:
                    text = mf.read()
            except Exception:
                continue
            text_no_code = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
            for m in url_pattern.finditer(text_no_code):
                u = m.group(0).rstrip('.,;:)"')
                ext_links.append((fp.replace('\\', '/'), u))

print(f"Total external link occurrences: {len(ext_links)}")
unique_urls = sorted(set(u for _, u in ext_links))
print(f"Unique external URLs: {len(unique_urls)}")
