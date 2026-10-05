// Program to print array elements using recursion in C++
// This demonstrates how recursion can be used to traverse and print an array.

#include <iostream>
using namespace std;

// Recursive function to print array elements
// Parameters:
//   arr: pointer to the array
//   idx: current index to print
//   n: total number of elements in the array
void printArrayRecursive(const int* arr, int idx, int n) {
    // Base case: if index reaches the size of the array, stop recursion
    if (idx == n) {
        return;
    }
    // Print the current element
    cout << arr[idx] << " ";
    // Recursive call to print the next element
    printArrayRecursive(arr, idx + 1, n);
}

int main() {
    // Define and initialize the array
    int arr[] = {1, 3, 5, 6, 3};
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate array size

    cout << "Array elements printed using recursion: ";
    // Call the recursive function starting from index 0
    printArrayRecursive(arr, 0, n);

    cout << endl; // Print newline after all elements
    return 0;
}