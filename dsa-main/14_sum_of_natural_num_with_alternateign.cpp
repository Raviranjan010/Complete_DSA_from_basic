#include <iostream>
using namespace std;

// Recursive function to calculate sum of natural numbers till n with alternate signs
int sumOfNaturalNumWithAlternateSign(int n) {
    // Base case: if n is 0, return 0 (sum of zero numbers is zero)
    if (n == 0) return 0;

    // If n is even, subtract n; if odd, add n
    int sign = (n % 2 == 0) ? -1 : 1;

    // Recursive call: sum up to (n-1) plus current n with its sign
    return sumOfNaturalNumWithAlternateSign(n - 1) + sign * n;
}

int main() {
    cout << sumOfNaturalNumWithAlternateSign(7) << "\n"; // Output for n=7
    cout << sumOfNaturalNumWithAlternateSign(10) << "\n"; // Output for n=10
    cout << sumOfNaturalNumWithAlternateSign(5) << "\n"; // Output for n=5
    return 0;
}

