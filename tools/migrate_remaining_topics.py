import os
import shutil
import csv

ledger = []

# ==================== TOPIC 16: Strings Advanced ====================
os.makedirs('16-Strings-Advanced/concepts', exist_ok=True)
os.makedirs('16-Strings-Advanced/problems', exist_ok=True)
os.makedirs('16-Strings-Advanced/code/001-pattern-matching', exist_ok=True)

with open('16-Strings-Advanced/README.md', 'w', encoding='utf-8') as f:
    f.write('# 16 — Advanced Strings\n\nPrerequisites: `00-Start-Here`, `03-Arrays-and-Strings`\n\nAdvanced string algorithms: KMP pattern matching, Z-algorithm, Rabin-Karp rolling hash, Trie for strings, and suffix structures.\n')
ledger.append(('16-Strings-Advanced/README.md', 'NA', 'NA', 'Created topic hub README for Strings Advanced'))

src_pm = 'DSA_server-main/DSA-MasterCourse/03_Strings/code/pattern_matching.cpp'
if os.path.exists(src_pm):
    shutil.copy(src_pm, '16-Strings-Advanced/code/001-pattern-matching/solution.cpp')
    ledger.append(('16-Strings-Advanced/code/001-pattern-matching/solution.cpp', src_pm, 'NA', 'Migrated string pattern matching algorithms (naive & KMP preview)'))

c16 = '''# String Pattern Matching Algorithms: Naive & KMP

## 1. Problem Formulation
Given text $T$ of length $n$ and pattern $P$ of length $m$, find all occurrences of $P$ in $T$.

## 2. Naive Algorithm
$O((n - m + 1) \\times m)$ worst case.

## 3. Knuth-Morris-Pratt (KMP)
Constructs $\\pi$ table (longest proper prefix which is also suffix) in $O(m)$ time, achieving overall $O(n + m)$ search time.
'''
with open('16-Strings-Advanced/concepts/01-pattern-matching-kmp.md', 'w', encoding='utf-8') as f:
    f.write(c16)
ledger.append(('16-Strings-Advanced/concepts/01-pattern-matching-kmp.md', 'NA', 'NA', 'Created KMP pattern matching concept guide'))


# ==================== TOPIC 17: Advanced Data Structures ====================
os.makedirs('17-Advanced-Data-Structures/concepts', exist_ok=True)
os.makedirs('17-Advanced-Data-Structures/problems', exist_ok=True)
os.makedirs('17-Advanced-Data-Structures/code/001-trie-implementation', exist_ok=True)

with open('17-Advanced-Data-Structures/README.md', 'w', encoding='utf-8') as f:
    f.write('# 17 — Advanced Data Structures\n\nPrerequisites: `00-Start-Here`, `10-Trees`\n\nSpecialized tree and graph structures: Trie (Prefix Tree), Disjoint Set Union (DSU / Union-Find with path compression), Segment Tree (point/range query), and Fenwick Tree (Binary Indexed Tree).\n')
ledger.append(('17-Advanced-Data-Structures/README.md', 'NA', 'NA', 'Created topic hub README for Advanced Data Structures'))

c17_trie = 'DSA_server-main/DSA-MasterCourse/13_Tries/13_notes.md'
if os.path.exists(c17_trie):
    with open(c17_trie, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open('17-Advanced-Data-Structures/concepts/01-trie-prefix-tree-guide.md', 'w', encoding='utf-8') as f_out:
            f_out.write(f_in.read())
    ledger.append(('17-Advanced-Data-Structures/concepts/01-trie-prefix-tree-guide.md', c17_trie, 'NA', 'Preserved Trie prefix tree notes and operations'))

c17_segtree = 'DSA_server-main/DSA-MasterCourse/19_Segment_Tree_and_BIT/19_notes.md'
if os.path.exists(c17_segtree):
    with open(c17_segtree, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open('17-Advanced-Data-Structures/concepts/02-segment-tree-and-fenwick-tree.md', 'w', encoding='utf-8') as f_out:
            f_out.write(f_in.read())
    ledger.append(('17-Advanced-Data-Structures/concepts/02-segment-tree-and-fenwick-tree.md', c17_segtree, 'NA', 'Preserved Segment Tree and Binary Indexed Tree notes'))

trie_code = '''// Trie (Prefix Tree) implementation in C++
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct TrieNode {
    TrieNode* children[26];
    bool isEndOfWord;
    TrieNode() : isEndOfWord(false) {
        for (int i = 0; i < 26; i++) children[i] = nullptr;
    }
};

class Trie {
    TrieNode* root;
public:
    Trie() { root = new TrieNode(); }

    void insert(const string& word) {
        TrieNode* curr = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!curr->children[idx]) curr->children[idx] = new TrieNode();
            curr = curr->children[idx];
        }
        curr->isEndOfWord = true;
    }

    bool search(const string& word) {
        TrieNode* curr = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!curr->children[idx]) return false;
            curr = curr->children[idx];
        }
        return curr->isEndOfWord;
    }

    bool startsWith(const string& prefix) {
        TrieNode* curr = root;
        for (char c : prefix) {
            int idx = c - 'a';
            if (!curr->children[idx]) return false;
            curr = curr->children[idx];
        }
        return true;
    }
};

int main() {
    Trie trie;
    trie.insert("apple");
    cout << "Search 'apple': " << (trie.search("apple") ? "Found" : "Not Found") << endl;
    cout << "Search 'app': " << (trie.search("app") ? "Found" : "Not Found") << endl;
    cout << "Starts with 'app': " << (trie.startsWith("app") ? "Yes" : "No") << endl;
    return 0;
}
'''
with open('17-Advanced-Data-Structures/code/001-trie-implementation/solution.cpp', 'w', encoding='utf-8') as f_code:
    f_code.write(trie_code)
ledger.append(('17-Advanced-Data-Structures/code/001-trie-implementation/solution.cpp', 'NA', 'NA', 'Created complete Trie insertion, search, and prefix matching solution'))


# ==================== TOPIC 18: Advanced Algorithms ====================
os.makedirs('18-Advanced-Algorithms/concepts', exist_ok=True)
os.makedirs('18-Advanced-Algorithms/problems', exist_ok=True)

with open('18-Advanced-Algorithms/README.md', 'w', encoding='utf-8') as f:
    f.write('# 18 — Advanced Algorithms\n\nPrerequisites: `13-Graphs`, `14-Dynamic-Programming`, `17-Advanced-Data-Structures`\n\nCompetitive programming patterns: Tarjan’s strongly connected components, Bridges & Articulation Points, Lowest Common Ancestor (Binary Lifting), and Euler Tour.\n')
ledger.append(('18-Advanced-Algorithms/README.md', 'NA', 'NA', 'Created topic hub README for Advanced Algorithms'))

c18_cp = 'DSA_server-main/DSA-MasterCourse/22_Competitive_Programming_Extras/22_notes.md'
if os.path.exists(c18_cp):
    with open(c18_cp, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open('18-Advanced-Algorithms/concepts/01-competitive-programming-patterns.md', 'w', encoding='utf-8') as f_out:
            f_out.write(f_in.read())
    ledger.append(('18-Advanced-Algorithms/concepts/01-competitive-programming-patterns.md', c18_cp, 'NA', 'Preserved competitive programming extras and advanced tricks'))


# ==================== TOPIC 19: Interview Preparation ====================
os.makedirs('19-Interview-Preparation/company-questions', exist_ok=True)
os.makedirs('19-Interview-Preparation/mock-assessments', exist_ok=True)

with open('19-Interview-Preparation/README.md', 'w', encoding='utf-8') as f:
    f.write('# 19 — Interview Preparation\n\nCurated high-frequency company interview problem sheets, patterns checklist, behavioral tips, and timed mock assessments.\n')
ledger.append(('19-Interview-Preparation/README.md', 'NA', 'NA', 'Created topic hub README for Interview Preparation'))

companies = ['Adobe', 'Amazon', 'Flipkart', 'Google', 'Meta', 'Microsoft', 'TCS_Infosys_Wipro']
for comp in companies:
    src_comp = f'DSA_server-main/DSA-MasterCourse/23_Interview_Questions_by_Company/{comp}.md'
    target_comp = f'19-Interview-Preparation/company-questions/{comp.lower()}.md'
    if os.path.exists(src_comp):
        with open(src_comp, 'r', encoding='utf-8', errors='ignore') as f_in:
            with open(target_comp, 'w', encoding='utf-8') as f_out:
                f_out.write(f_in.read())
        ledger.append((target_comp, src_comp, 'NA', f'Preserved {comp} interview question collection'))

src_arr_int = 'DSA_server-main/DSA-MasterCourse/02_Arrays/11_Interview_Prep/Arrays_Interview.md'
if os.path.exists(src_arr_int):
    with open(src_arr_int, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open('19-Interview-Preparation/company-questions/arrays-interview-handbook.md', 'w', encoding='utf-8') as f_out:
            f_out.write(f_in.read())
    ledger.append(('19-Interview-Preparation/company-questions/arrays-interview-handbook.md', src_arr_int, 'NA', 'Preserved array interview handbook'))

src_daily = 'Summer_pep_DSA-main/Daily problems/Practice-Problems.md'
if os.path.exists(src_daily):
    with open(src_daily, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open('19-Interview-Preparation/mock-assessments/daily-practice-problems.md', 'w', encoding='utf-8') as f_out:
            f_out.write(f_in.read())
    ledger.append(('19-Interview-Preparation/mock-assessments/daily-practice-problems.md', src_daily, 'NA', 'Preserved daily practice problem sets'))


# ==================== TOPIC 20: Cheatsheets ====================
os.makedirs('20-Cheatsheets', exist_ok=True)
cheats = [
    'complexity-cheatsheet.md', 'cpp-stl-cheatsheet.md', 'dp-patterns-cheatsheet.md',
    'graph-algorithms-cheatsheet.md', 'interview-last-minute-revision.md',
    'recursion-cheatsheet.md', 'sorting-cheatsheet.md'
]
for ch in cheats:
    src_ch = f'CHEATSHEETS/{ch}'
    target_ch = f'20-Cheatsheets/{ch}'
    if os.path.exists(src_ch):
        shutil.copy(src_ch, target_ch)
        ledger.append((target_ch, src_ch, 'NA', f'Preserved {ch} for Phase 5 content expansion'))

with open('20-Cheatsheets/README.md', 'w', encoding='utf-8') as f:
    f.write('# 20 — High-Yield Cheatsheets\n\nQuick revision guides for time complexity, STL containers, recursion patterns, DP templates, and graph algorithms.\n')
ledger.append(('20-Cheatsheets/README.md', 'NA', 'NA', 'Created cheatsheets hub README'))


# ==================== EXTRAS ====================
os.makedirs('_extras/wasm-student-record', exist_ok=True)
os.makedirs('_extras/console-projects', exist_ok=True)
os.makedirs('_extras/web-tutorials', exist_ok=True)

wasm_files = ['build.bat', 'deploy.bat', 'serve.bat', 'verify.bat', 'README.md']
for wf in wasm_files:
    src_wf = f'dsa-main/{wf}'
    if os.path.exists(src_wf):
        shutil.copy(src_wf, f'_extras/wasm-student-record/{wf}')
        ledger.append((f'_extras/wasm-student-record/{wf}', src_wf, 'NA', 'Categorized Emscripten WebAssembly student record build/deploy script as EXTRA'))

if os.path.exists('dsa-main/LibraryManagement.cpp'):
    shutil.copy('dsa-main/LibraryManagement.cpp', '_extras/console-projects/LibraryManagement.cpp')
    ledger.append(('_extras/console-projects/LibraryManagement.cpp', 'dsa-main/LibraryManagement.cpp', 'NA', 'Categorized Library Management console project as EXTRA'))

if os.path.exists('DSA_final-main/index.html'):
    shutil.copy('DSA_final-main/index.html', '_extras/web-tutorials/html-form-guide.html')
    ledger.append(('_extras/web-tutorials/html-form-guide.html', 'DSA_final-main/index.html', 'NA', 'Categorized HTML form tutorial demo as EXTRA'))


# ==================== ARCHIVE ====================
os.makedirs('_archive/DSA_server-main', exist_ok=True)
os.makedirs('_archive/legacy-planning', exist_ok=True)
os.makedirs('_archive/dsa-main', exist_ok=True)

server_archives = ['CLAUDE.md', 'DSA-MasterCourse/status.txt', 'DSA-MasterCourse/ROADMAP.md', 'DSA-MasterCourse/STUDY_PLAN.md']
for sa in server_archives:
    src_sa = f'DSA_server-main/{sa}'
    fn = os.path.basename(sa)
    if os.path.exists(src_sa):
        shutil.copy(src_sa, f'_archive/DSA_server-main/{fn}')
        ledger.append((f'_archive/DSA_server-main/{fn}', src_sa, 'NA', 'Archived legacy status/instruction file in _archive/'))

root_plans = ['00-MASTER-PROMPT.md', '01-REPO-STRUCTURE-AND-NAMING.md', '02-COMPLETE-DSA-CURRICULUM.md', '03-CONTENT-STANDARDS-AND-TEMPLATE.md', '04-EXECUTION-PLAN-AND-PROMPTS.md']
for rp in root_plans:
    if os.path.exists(rp):
        shutil.copy(rp, f'_archive/legacy-planning/{rp}')
        ledger.append((f'_archive/legacy-planning/{rp}', rp, 'NA', 'Archived legacy planning file in _archive/'))

if os.path.exists('DSA_final-main/commit.txt'):
    shutil.copy('DSA_final-main/commit.txt', '_archive/commit.txt')
    ledger.append(('_archive/commit.txt', 'DSA_final-main/commit.txt', 'NA', 'Archived non-empty scratch commit commands in _archive/'))

if os.path.exists('dsa-main/tempCodeRunnerFile.cpp'):
    shutil.copy('dsa-main/tempCodeRunnerFile.cpp', '_archive/dsa-main/tempCodeRunnerFile.cpp')
    ledger.append(('_archive/dsa-main/tempCodeRunnerFile.cpp', 'dsa-main/tempCodeRunnerFile.cpp', 'NA', 'Archived non-empty temp runner file in _archive/'))

if os.path.exists('dsa-main/.gitignore'):
    shutil.copy('dsa-main/.gitignore', '_archive/dsa-main/.gitignore')
    ledger.append(('_archive/dsa-main/.gitignore', 'dsa-main/.gitignore', 'NA', 'Archived sub-project gitignore in _archive/'))


with open('_meta/MERGE_LEDGER.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ledger:
        writer.writerow(row)

print(f'Migrated Topics 16-20, Extras, and Archive: {len(ledger)} actions logged')
