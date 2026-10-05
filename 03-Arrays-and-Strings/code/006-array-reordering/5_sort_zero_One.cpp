#include <iostream>
#include <vector>
using namespace std;

// Function to sort a vector containing only 0's and 1's
void sortZerosAndOnes(vector<int> &v) {
    int left = 0, right = v.size() - 1;

    // Loop until the two pointers meet
    while (left < right) {

        // If left is 1 and right is 0, swap them
        if (v[left] == 1 && v[right] == 0) {
            v[left++] = 0;
            v[right--] = 1;
        }

        // If left is already 0, move left pointer to the right
        if (v[left] == 0) {
            left++;
        }

        // If right is already 1, move right pointer to the left
        if (v[right] == 1) {
            right--;
        }
    }
}

int main() {
    int n;
    cout << "Enter number of elements (only 0's and 1's allowed): ";
    cin >> n;

    vector<int> v(n);
    cout << "Enter " << n << " elements (0 or 1 only):" << endl;
    
    // Taking input
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    // Sort 0's to the left and 1's to the right
    sortZerosAndOnes(v);

    cout << "Sorted Array: ";
    for (int num : v) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
