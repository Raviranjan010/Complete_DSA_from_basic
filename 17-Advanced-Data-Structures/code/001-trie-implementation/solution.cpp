// Trie (Prefix Tree) implementation in C++
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
