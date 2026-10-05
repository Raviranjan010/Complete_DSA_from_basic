// Binary Search Tree insertion and search in C++
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
