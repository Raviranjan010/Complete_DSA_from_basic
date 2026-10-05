// Essential Bit Manipulation tricks in C++
#include <iostream>
using namespace std;

bool isPowerOfTwo(int n) {
    return n > 0 && (n & (n - 1)) == 0;
}

int countSetBits(int n) {
    int count = 0;
    while (n > 0) {
        n = n & (n - 1); // Clears the lowest set bit
        count++;
    }
    return count;
}

int main() {
    int x = 16;
    cout << x << " is power of two: " << (isPowerOfTwo(x) ? "Yes" : "No") << endl;

    int y = 29; // Binary: 11101
    cout << "Set bits in " << y << ": " << countSetBits(y) << endl;

    return 0;
}
