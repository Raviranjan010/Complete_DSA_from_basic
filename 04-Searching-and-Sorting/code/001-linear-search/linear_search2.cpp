// Linear search algorithm implementation in C++14
// if element is not found, print a message
#include <iostream>
int main() {
    int arr1[] = {10, 20, 30, 40, 50};

    int n = sizeof(arr1) / sizeof(arr1[0]); // Calculate the number of elements in the array
    int key = 60; // Element to search for
    bool found = false; // Flag to indicate if the element is found

    for (int i = 0; i < n; i++) {
        if (arr1[i] == key) {
            found = true; // Element found
            std::cout << "Element " << key << " found at index " << i << std::endl;
            break; // Exit the loop once the element is found
        }
    }

    if (!found) {
        std::cout << "Element " << key << " not found in the array." << std::endl;
    }

    return 0;
}