// Sum of Array Elements Using Recursion
// This program demonstrates how to calculate the sum of all elements in an array using a recursive approach.

#include <iostream>
using namespace std;

// Recursive function to calculate the sum of array elements
int sumArray(const int* arr, int idx, int n) {
    // Base case: if index reaches the end of the array, return 0
    if (idx == n)
        return 0;
    // Recursive case: add current element to the sum of the remaining elements
    return arr[idx] + sumArray(arr, idx + 1, n);
}

int main() {
    int arr[] = {1, 2, 3, 4, 5}; // Example array
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the number of elements in the array

    int sum = sumArray(arr, 0, n); // Start recursion from index 0
    cout << "Sum of array elements: " << sum << endl;

    return 0;
}
