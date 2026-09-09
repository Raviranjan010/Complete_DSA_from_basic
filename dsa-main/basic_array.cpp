// Array is a collection of elements of the same type, stored in contiguous memory locations.
#include <iostream>
int main() {
    // Declare an array of integers with 5 elements
    int arr[5] = {10, 20, 30, 40, 50};
    // Print the size of the array
    std::cout << "Size of the array: " << sizeof(arr) / sizeof(arr[0]) << " elements" << std::endl;
    // print number of elements in the array
    std::cout << "Number of elements in the array: " << sizeof(arr) / sizeof(arr[0]) << std::endl;
    // Access and print each element of the array
    for (int i = 0; i < 5; i++) {
        std::cout << "Element at index " << i << ": " << arr[i] << std::endl;
    }

    // Modify an element in the array
    arr[2] = 100;
    std::cout << "After modification, element at index 2: " << arr[2] << std::endl;

    return 0;
}