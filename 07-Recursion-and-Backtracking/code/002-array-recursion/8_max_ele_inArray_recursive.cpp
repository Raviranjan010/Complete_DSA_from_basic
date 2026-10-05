#include <iostream>
using namespace std;

// Recursive function to find the maximum element in an array
int findMax(const int arr[], int idx, int n) {
    // Base case: If only one element is left, return it
    if (idx == n - 1) {
        return arr[idx];
    }
    // Recursive case: Find the maximum in the rest of the array
    int maxInRest = findMax(arr, idx + 1, n);
    return (arr[idx] > maxInRest) ? arr[idx] : maxInRest;
}

int main() {
    int arr[] = {2, 3, 5, 7, 8, 3};
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate array size dynamically

    cout << "Array elements: ";
    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;

    int maximum = findMax(arr, 0, n);
    cout << "Maximum element in the array: " << maximum << endl;

    return 0;
}

// This program demonstrates how to find the maximum element in an array using recursion.
// The function 'findMax' compares the current element with the maximum of the remaining elements.
