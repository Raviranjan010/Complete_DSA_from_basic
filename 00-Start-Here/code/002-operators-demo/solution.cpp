// Comprehensive demonstration of Operators in C++
#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 3;

    // Arithmetic Operators
    cout << "Arithmetic: " << (a + b) << ", " << (a - b) << ", " << (a * b) << ", " << (a / b) << ", " << (a % b) << endl;

    // Relational Operators
    cout << "Relational (a > b): " << (a > b) << ", (a == b): " << (a == b) << endl;

    // Logical Operators
    cout << "Logical ((a > 5) && (b < 5)): " << ((a > 5) && (b < 5)) << endl;

    // Assignment & Compound Operators
    int c = a;
    c += 5;
    cout << "Compound assignment (c += 5): " << c << endl;

    // Bitwise Operators
    cout << "Bitwise (a & b): " << (a & b) << ", (a | b): " << (a | b) << ", (a ^ b): " << (a ^ b) << endl;

    return 0;
}