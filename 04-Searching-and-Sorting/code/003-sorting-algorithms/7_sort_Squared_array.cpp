// Sort squared array using two-pointer technique in O(n) time
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

void sortedSquaredArray(const vector<int>& v) {
    int n = v.size();
    vector<int> ans(n);
    int left_ptr = 0;
    int right_ptr = n - 1;
    int k = n - 1;

    while (left_ptr <= right_ptr) {
        if (abs(v[left_ptr]) < abs(v[right_ptr])) {
            ans[k--] = v[right_ptr] * v[right_ptr];
            right_ptr--;
        } else {
            ans[k--] = v[left_ptr] * v[left_ptr];
            left_ptr++;
        }
    }

    for (int i = 0; i < n; i++) {
        cout << ans[i] << (i + 1 < n ? " " : "");
    }
    cout << endl;
}

int main() {
    int n;
    if (cin >> n) {
        vector<int> v(n);
        for (int i = 0; i < n; i++) {
            cin >> v[i];
        }
        sortedSquaredArray(v);
    }
    return 0;
}