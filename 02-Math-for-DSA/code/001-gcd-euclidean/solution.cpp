#include <iostream>

// Recursive function to compute GCD using Euclidean algorithm
int gcd(int a, int b) {
    if (b == 0)
        return a; // Base case: if b is 0, a is the GCD
    return gcd(b, a % b); // Recursive case
}

int main() {
    int a, b;
    std::cout << "Enter two integers: ";
    std::cin >> a >> b;
    std::cout << "GCD of " << a << " and " << b << " is: " << gcd(a, b) << std::endl;
    return 0;
}
