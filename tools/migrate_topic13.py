import os
import shutil
import csv

os.makedirs('13-Graphs/concepts', exist_ok=True)
os.makedirs('13-Graphs/problems', exist_ok=True)
os.makedirs('13-Graphs/code', exist_ok=True)

ledger = []

# README
with open('13-Graphs/README.md', 'w', encoding='utf-8') as f:
    f.write('# 13 — Graphs\n\nPrerequisites: `00-Start-Here`, `01-Complexity-Analysis`, `09-Stack-and-Queue`, `10-Trees`, `11-Heap-and-Priority-Queue`\n\nGraph representations (adjacency matrix vs list), BFS, DFS, cycle detection, topological sort (Kahn’s algorithm), shortest paths (Dijkstra, Bellman-Ford, Floyd-Warshall), and MST.\n')
ledger.append(('13-Graphs/README.md', 'NA', 'NA', 'Created topic hub README for Graphs'))

# Concepts
c1_base = 'DSA_server-main/DSA-MasterCourse/14_Graphs/14_notes.md'
target_c1 = '13-Graphs/concepts/01-graph-representations-and-traversals.md'
if os.path.exists(c1_base):
    with open(c1_base, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open(target_c1, 'w', encoding='utf-8') as f_out:
            f_out.write(f_in.read())
    ledger.append((target_c1, c1_base, 'NA', 'Preserved graph representation, BFS/DFS, cycle detection, and topological sort'))

c2_base = 'DSA_server-main/DSA-MasterCourse/20_Advanced_Graphs/20_notes.md'
target_c2 = '13-Graphs/concepts/02-shortest-paths-and-advanced-graphs.md'
if os.path.exists(c2_base):
    with open(c2_base, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open(target_c2, 'w', encoding='utf-8') as f_out:
            f_out.write(f_in.read())
    ledger.append((target_c2, c2_base, 'NA', 'Preserved shortest path algorithms: Dijkstra, Bellman-Ford, and Floyd-Warshall'))

# Code
os.makedirs('13-Graphs/code/001-graph-traversals', exist_ok=True)
code1 = '''// Graph BFS and DFS traversals in C++ using adjacency list
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void bfs(int start, const vector<vector<int>>& adj, int n) {
    vector<bool> visited(n, false);
    queue<int> q;

    visited[start] = true;
    q.push(start);

    cout << "BFS traversal: ";
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        cout << u << " ";

        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }
    cout << endl;
}

void dfsHelper(int u, const vector<vector<int>>& adj, vector<bool>& visited) {
    visited[u] = true;
    cout << u << " ";
    for (int v : adj[u]) {
        if (!visited[v]) {
            dfsHelper(v, adj, visited);
        }
    }
}

void dfs(int start, const vector<vector<int>>& adj, int n) {
    vector<bool> visited(n, false);
    cout << "DFS traversal: ";
    dfsHelper(start, adj, visited);
    cout << endl;
}

int main() {
    int n = 5;
    vector<vector<int>> adj(n);
    adj[0] = {1, 2};
    adj[1] = {0, 3};
    adj[2] = {0, 4};
    adj[3] = {1};
    adj[4] = {2};

    bfs(0, adj, n);
    dfs(0, adj, n);

    return 0;
}
'''
with open('13-Graphs/code/001-graph-traversals/solution.cpp', 'w', encoding='utf-8') as f_code:
    f_code.write(code1)
ledger.append(('13-Graphs/code/001-graph-traversals/solution.cpp', 'NA', 'NA', 'Created BFS and DFS graph traversals implementation'))

with open('_meta/MERGE_LEDGER.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ledger:
        writer.writerow(row)

print(f'Migrated Topic 13: {len(ledger)} actions logged')
