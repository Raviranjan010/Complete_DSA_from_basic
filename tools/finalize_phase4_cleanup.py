import os
import shutil

# Remove the five raw source repositories (all contents are merged, moved, archived, or extras)
sources = [
    'DSA_ac-main',
    'DSA_final-main',
    'DSA_server-main',
    'dsa-main',
    'Summer_pep_DSA-main'
]

for src in sources:
    if os.path.exists(src):
        shutil.rmtree(src)
        print(f'Removed source folder: {src}')

# Remove legacy lowercase numbered folders and CHEATSHEETS
old_skeletons = [
    '00-prerequisites',
    '01-complexity-analysis',
    '02-arrays-and-strings',
    '03-recursion-and-backtracking',
    '04-linked-list',
    '05-stack-and-queue',
    '06-hashing',
    '07-trees',
    '08-heaps-and-priority-queue',
    '09-graphs',
    '10-greedy',
    '11-dynamic-programming',
    '12-advanced-strings',
    '13-bit-manipulation-and-math',
    '14-advanced-topics',
    '15-interview-prep',
    'CHEATSHEETS'
]

for skel in old_skeletons:
    # On Windows, be careful not to delete capitalized newly populated directories if they share the name!
    # Check if newly populated directories like 01-Complexity-Analysis exist
    # Let's inspect before deleting
    pass

# Delete truly 0-byte file DSA_MASTER_PROMPT.md
if os.path.exists('DSA_MASTER_PROMPT.md') and os.path.getsize('DSA_MASTER_PROMPT.md') == 0:
    os.remove('DSA_MASTER_PROMPT.md')
    print('Removed 0-byte DSA_MASTER_PROMPT.md')

# Delete legacy root planning files (already archived in _archive/legacy-planning)
root_plans = [
    '00-MASTER-PROMPT.md',
    '01-REPO-STRUCTURE-AND-NAMING.md',
    '02-COMPLETE-DSA-CURRICULUM.md',
    '03-CONTENT-STANDARDS-AND-TEMPLATE.md',
    '04-EXECUTION-PLAN-AND-PROMPTS.md'
]
for rp in root_plans:
    if os.path.exists(rp):
        os.remove(rp)
        print(f'Removed root legacy file (archived): {rp}')

print('Source cleanup finished.')
