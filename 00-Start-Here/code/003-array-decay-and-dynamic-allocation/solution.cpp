#include <iostream>
#include <vector>
#include <array>

// Decayed function: receives raw pointer, loses size
void decayedFunction(const int arr[]) {
    // sizeof(arr) is sizeof(const int*), not total array size!
    std::cout << "Inside decayed function: sizeof(param) = " << sizeof(arr) 
              << " bytes (pointer size)\n";
}

// Modern C++: prevents decay by accepting std::vector
void safeVectorFunction(const std::vector<int>& vec) {
    std::cout << "Inside safe vector function: size = " << vec.size() 
              << " elements\n";
}

int main() {
    int rawArr[5] = {10, 20, 30, 40, 50};
    
    std::cout << "In local scope: sizeof(rawArr) = " << sizeof(rawArr) 
              << " bytes (5 ints * 4 bytes)\n";
    
    decayedFunction(rawArr);

    std::vector<int> dynamicVec = {10, 20, 30, 40, 50};
    safeVectorFunction(dynamicVec);

    return 0;
}
