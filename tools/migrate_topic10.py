import os
import shutil
import csv

os.makedirs('10-Trees/concepts', exist_ok=True)
os.makedirs('10-Trees/problems', exist_ok=True)
os.makedirs('10-Trees/code', exist_ok=True)

ledger = []

# README
with open('10-Trees/README.md', 'w', encoding='utf-8') as f:
    f.write('# 10 — Trees (Binary Trees and BST)\n\nPrerequisites: `00-Start-Here` (Pointers), `01-Complexity-Analysis`, `07-Recursion-and-Backtracking`, `09-Stack-and-Queue`\n\nHierarchical non-linear data structures: Binary Trees, Traversals (Inorder, Preorder, Postorder, Level-Order), Height, Diameter, LCA, and Binary Search Trees (BST).\n')
ledger.append(('10-Trees/README.md', 'NA', 'NA', 'Created topic hub README for Trees'))

# Concepts
c1_base = 'DSA_server-main/DSA-MasterCourse/10_Trees/10_notes.md'
target_c1 = '10-Trees/concepts/01-binary-trees-fundamentals-and-traversals.md'
if os.path.exists(c1_base):
    with open(c1_base, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open(target_c1, 'w', encoding='utf-8') as f_out:
            f_out.write(f_in.read())
    ledger.append((target_c1, c1_base, 'NA', 'Preserved binary trees structure, properties, and DFS/BFS traversals'))

c2_base = 'DSA_server-main/DSA-MasterCourse/11_Binary_Search_Tree/11_notes.md'
target_c2 = '10-Trees/concepts/02-binary-search-tree-properties-and-ops.md'
if os.path.exists(c2_base):
    with open(c2_base, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open(target_c2, 'w', encoding='utf-8') as f_out:
            f_out.write(f_in.read())
    ledger.append((target_c2, c2_base, 'NA', 'Preserved BST properties, search, insert, and delete operations'))

# Code
os.makedirs('10-Trees/code/001-binary-tree-traversals', exist_ok=True)
code1 = '''// Binary tree construction and DFS traversals in C++
#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

void inorder(TreeNode* root) {
    if (!root) return;
    inorder(root->left);
    cout << root->val << " ";
    inorder(root->right);
}

void preorder(TreeNode* root) {
    if (!root) return;
    cout << root->val << " ";
    preorder(root->left);
    preorder(root->right);
}

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    cout << "Inorder traversal: ";
    inorder(root);
    cout << endl;

    cout << "Preorder traversal: ";
    preorder(root);
    cout << endl;

    return 0;
}
'''
with open('10-Trees/code/001-binary-tree-traversals/solution.cpp', 'w', encoding='utf-8') as f_code:
    f_code.write(code1)
ledger.append(('10-Trees/code/001-binary-tree-traversals/solution.cpp', 'NA', 'NA', 'Created binary tree traversals implementation'))

os.makedirs('10-Trees/code/002-bst-operations', exist_ok=True)
code2 = '''// Binary Search Tree insertion and search in C++
#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

TreeNode* insert(TreeNode* root, int val) {
    if (!root) return new TreeNode(val);
    if (val < root->val) root->left = insert(root->left, val);
    else root->right = insert(root->right, val);
    return root;
}

bool search(TreeNode* root, int val) {
    if (!root) return false;
    if (root->val == val) return true;
    if (val < root->val) return search(root->left, val);
    return search(root->right, val);
}

int main() {
    TreeNode* root = nullptr;
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 70);
    insert(root, 20);

    cout << "Search 30: " << (search(root, 30) ? "Found" : "Not Found") << endl;
    cout << "Search 100: " << (search(root, 100) ? "Found" : "Not Found") << endl;
    return 0;
}
'''
with open('10-Trees/code/002-bst-operations/solution.cpp', 'w', encoding='utf-8') as f_code:
    f_code.write(code2)
ledger.append(('10-Trees/code/002-bst-operations/solution.cpp', 'NA', 'NA', 'Created BST insertion and search implementation'))

with open('_meta/MERGE_LEDGER.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ledger:
        writer.writerow(row)

print(f'Migrated Topic 10: {len(ledger)} actions logged')
