// Printing the factorial of a number using recursion in C++.
// This program calculates the factorial of a given number using a recursive function.
#include <iostream>
using namespace std;

// Function to calculate factorial using recursion
long long factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return (long long)n * factorial(n - 1);
}

int main() {
    int n;
    if (cin >> n) {
        cout << factorial(n) << endl;
    }
    return 0;
}