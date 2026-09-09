#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Step 1: Input number of elements
    int n;
    cout << "Enter the number of elements in the array: ";
    cin >> n;

    // Step 2: Declare vector (1-based indexing, so size n+1)
    vector<int> v(n + 1);

    cout << "Enter the elements of the array: ";
    for (int i = 1; i <= n; ++i) {
        cin >> v[i]; // Fill array from index 1 to n
    }

    // Step 3: Precompute prefix sum array for faster range sum queries
    vector<int> prefixSum(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        prefixSum[i] = prefixSum[i - 1] + v[i];
    }

    // Step 4: Process queries
    int q;
    cout << "Enter the number of queries: ";
    cin >> q;

    while (q--) {
        int l, r;
        cout << "Enter left and right indices (1-based): ";
        cin >> l >> r;

        // Use prefix sum to find sum in O(1) time
        int sum = prefixSum[r] - prefixSum[l - 1];

        cout << "Sum from index " << l << " to " << r << " is: " << sum << endl;
    }

    return 0;
}
