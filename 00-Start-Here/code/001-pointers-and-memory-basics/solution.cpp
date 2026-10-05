#include <iostream>

void demonstratePointerBasics() {
    int target = 10;
    int* ptr = &target;

    std::cout << "Initial scalar value: " << *ptr << "\n";
    std::cout << "Memory address of target: " << ptr << "\n";

    // Modify target indirectly via pointer
    *ptr = 42;
    std::cout << "Modified scalar value via pointer: " << target << "\n";

    // Pointer arithmetic on contiguous memory
    int arr[] = {10, 20, 30};
    int n = sizeof(arr) / sizeof(arr[0]);
    int* arrPtr = arr; // Decay to pointer to first element

    std::cout << "\nTraversing array via pointer arithmetic:\n";
    for (int i = 0; i < n; ++i) {
        std::cout << "Index " << i << ": Address = " << static_cast<void*>(arrPtr) 
                  << " | Value = " << *arrPtr << "\n";
        arrPtr++; // Advances by sizeof(int) bytes
    }
}

int main() {
    demonstratePointerBasics();
    return 0;
}
