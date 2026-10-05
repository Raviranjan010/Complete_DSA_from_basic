"""
Link checking verification tool for the consolidated repository.
Verifies all internal markdown links outside code blocks point to existing files.
"""

import os
import re
from pathlib import Path

def check_all_links():
    broken = []
    checked = 0
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    for root, dirs, files in os.walk('.'):
        # Exclude git, meta, and archive
        if root == '.' or '.git' in Path(root).parts or '_meta' in Path(root).parts or '_archive' in Path(root).parts:
            continue
        for f in files:
            if not f.endswith('.md'):
                continue
            file_path = os.path.join(root, f)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as md_file:
                content = md_file.read()

            # Remove fenced code blocks so ASCII diagrams like [16](3-4) are not treated as links
            content_no_code = re.sub(r'```.*?```', '', content, flags=re.DOTALL)

            for match in link_pattern.finditer(content_no_code):
                label, url = match.groups()
                # Ignore external URLs, anchor links, and mailto
                if url.startswith(('http://', 'https://', 'mailto:', '#')):
                    continue
                clean_url = url.split('#')[0]
                if not clean_url:
                    continue

                checked += 1
                target_path = os.path.normpath(os.path.join(root, clean_url))
                if not os.path.exists(target_path):
                    broken.append((file_path, url, target_path))

    return checked, broken

if __name__ == '__main__':
    checked, broken = check_all_links()
    print(f'Total internal links checked: {checked}')
    print(f'Total broken links: {len(broken)}')
    if broken:
        for src, url, tgt in broken:
            print(f'  {src} -> {url}')
