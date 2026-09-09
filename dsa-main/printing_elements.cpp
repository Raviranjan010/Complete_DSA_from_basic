// Using foreach loop to print elements of an array
#include <iostream>
#include <array>
int main() {
    // Declare an array of integers with 5 elements
    std::array<int, 5> arr = {10, 20, 30, 40, 50};

    // Print the size of the array
    std::cout << "Size of the array: " << arr.size() << " elements" << std::endl;

    // Print number of elements in the array
    std::cout << "Number of elements in the array: " << arr.size() << std::endl;

    // Access and print each element of the array using a range-based for loop
    for (const auto& element : arr) {
        std::cout << "Element: " << element << std::endl;
    }

    return 0;
}