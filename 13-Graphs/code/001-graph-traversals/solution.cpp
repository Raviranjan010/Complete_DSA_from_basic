// Graph BFS and DFS traversals in C++ using adjacency list
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
