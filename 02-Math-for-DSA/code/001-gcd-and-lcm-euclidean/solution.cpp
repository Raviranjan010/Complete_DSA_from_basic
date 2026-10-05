#include <iostream>
#include <numeric>

long long computeGcd(long long a, long long b) {
    while (b != 0) {
        long long rem = a % b;
        a = b;
        b = rem;
    }
    return a;
}

long long computeLcm(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / computeGcd(a, b)) * b;
}

int main() {
    long long a = 48, b = 18;
    std::cout << "GCD(" << a << ", " << b << ") = " << computeGcd(a, b) << "\n";
    std::cout << "LCM(" << a << ", " << b << ") = " << computeLcm(a, b) << "\n";
    return 0;
}
