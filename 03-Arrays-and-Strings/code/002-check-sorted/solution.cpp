// sorting algorithm: This project uses the C++ standard library's sorting algorithm.
// // This code demonstrates how to sort a vector of integers in C++ using the standard library's sort function.3
#include<iostream>
#include<vector>
using namespace std;
int main() {
    int arr[] = {1,2 ,3,4,5,6 }; // Initialize an array of integers


    bool isSorted = true; // Flag to check if the array is sorted
    // Print the sorted vector
    for(int i=1;i<=6;i++){
        if(arr[i-1]>arr[i]){
            isSorted = false; // If any element is greater than the next, the array is not sorted
            break;
        }
    }
    if(isSorted) {
        cout << "The array is already sorted." << endl; // If the array is sorted, print a message
    } else {
        cout << "The array is not sorted." << endl; // If the array is not sorted, print a message
    }
    cout << endl;
    // Sort the array using the standard library's sort function
    return 0; // Indicate successful execution

}