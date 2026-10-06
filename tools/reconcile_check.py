import csv
import os

with open('_meta/MANIFEST.csv', encoding='utf-8') as f:
    manifest = list(csv.DictReader(f))

with open('_meta/MERGE_LEDGER.csv', encoding='utf-8') as f:
    ledger = list(csv.DictReader(f))

print(f"Total manifest rows: {len(manifest)}")
print(f"Total ledger rows: {len(ledger)}")

# Categorize manifest entries
junk = [m for m in manifest if m['is_junk'] == 'yes']
print(f"Junk count: {len(junk)}")

# Check extras and archive
extras = []
archive = []
for m in manifest:
    p = m['path']
    if 'wasm' in p or 'LibraryManagement' in p or 'html-form' in p:
        extras.append(m)
    elif '_archive' in p or 'legacy-planning' in p or 'status.txt' in p or 'ROADMAP.md' in p or 'STUDY_PLAN.md' in p or 'CLAUDE.md' in p or 'commit.txt' in p or 'tempCodeRunnerFile.cpp' in p:
        archive.append(m)

print(f"Potential extras: {len(extras)}")
print(f"Potential archive: {len(archive)}")

# Let's inspect all manifest paths that were considered "rewritten"
# In MIGRATION_MAP.md or DECISIONS.md or AUDIT_REPORT.md:
for m in manifest:
    p = m['path']
    # If in numbered-folders or CHEATSHEETS or root README
    if p.startswith('CHEATSHEETS/') or (m['origin'] == 'numbered-folders' and p.endswith('README.md')) or p == 'README.md' or p == 'PROGRESS-TRACKER.md':
        print("Candidate rewritten:", p, m['origin'])
