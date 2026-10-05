#include <iostream>
#include <vector>

// Pass-by-value: copies are made on function stack
void swapByValue(int x, int y) {
    int temp = x;
    x = y;
    y = temp;
}

// Pass-by-reference: aliases caller's variables directly
void swapByReference(int& x, int& y) {
    int temp = x;
    x = y;
    y = temp;
}

// Pass-by-const-reference: zero-copy read-only access
void processLargeData(const std::vector<int>& data) {
    std::cout << "Read-only access to vector of size " << data.size() 
              << " without copying.\n";
}

int main() {
    int a = 15, b = 99;

    std::cout << "Before swap: a = " << a << ", b = " << b << "\n";

    swapByValue(a, b);
    std::cout << "After swapByValue: a = " << a << ", b = " << b << " (no change)\n";

    swapByReference(a, b);
    std::cout << "After swapByReference: a = " << a << ", b = " << b << " (swapped)\n";

    std::vector<int> numbers = {1, 2, 3, 4, 5};
    processLargeData(numbers);

    return 0;
}
