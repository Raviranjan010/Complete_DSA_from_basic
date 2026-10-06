import csv

with open('_meta/MERGE_LEDGER.csv', encoding='utf-8') as f:
    ledger = list(csv.DictReader(f))

found = []
for r in ledger:
    src = r['base_source'] + ' ' + r['contributed_from']
    if '02_Arrays' in src:
        found.append((r['base_source'], r['contributed_from'], r['new_path']))

print(f"Total 02_Arrays references in MERGE_LEDGER: {len(found)}")
for base, cont, newp in found:
    print(f"{base} | {cont} --> {newp}")
