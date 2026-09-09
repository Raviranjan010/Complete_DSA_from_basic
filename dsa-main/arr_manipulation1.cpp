// Manipulatio n of arrays in C++ can be done using the STL vector class.
// The vector class provides dynamic array functionality, allowing you to add, remove, and manipulate elements easily.
#include <iostream>
#include <vector>
using namespace std;
int main() {
    vector<int> arr = {1, 2, 3, 4, 5}; // Initialize a vector with some integers
    int target_sum = 6; // Define the target sum we want to find pairs for
    bool found = false; // Flag to indicate if any pair is found

    // Iterate through the vector to find pairs that sum up to target_sum
    for (int i = 0; i < arr.size(); i++) {
        for (int j = i + 1; j < arr.size(); j++) {
            if (arr[i] + arr[j] == target_sum) {
                cout << "Pair found: (" << arr[i] << ", " << arr[j] << ")" << endl;
                found = true; // Set flag to true if a pair is found
            }
        }
    }

    if (!found) {
        cout << "No pairs found that sum up to " << target_sum << endl; // If no pairs are found
    }

    return 0; // Indicate successful execution
}
