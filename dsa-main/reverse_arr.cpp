#include <iostream>
#include <vector>
#include <algorithm> // For reverse function
using namespace std;

int main() {
    vector<int> v = {1, 2, 3, 4, 5, 6, 7}; // Original vector
    int k = 3; // Number of positions to rotate

    k %= v.size(); // Ensure k is within bounds (important if k > v.size())

    // Step 1: Reverse the entire vector
    reverse(v.begin(), v.end());

    // Step 2: Reverse the first k elements
    reverse(v.begin(), v.begin() + k);

    // Step 3: Reverse the remaining elements
    reverse(v.begin() + k, v.end());

    // Print the rotated vector
    cout << "Rotated vector: ";
    for (int num : v) cout << num << " ";
    cout << endl;

    return 0;
}
