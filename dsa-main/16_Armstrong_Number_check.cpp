#include <iostream>
using namespace std;

// Recursive function to calculate base^exp
int power_recursive(int base, int exp) {
    if (exp == 0) return 1;
    if (exp % 2 == 0) {
        int half = power_recursive(base, exp / 2);
        return half * half;
    } else {
        int half = power_recursive(base, exp / 2);
        return base * half * half;
    }
}

// Recursive function to calculate sum of digits raised to the power of numDigits
int armstrong_sum(int n, int numDigits) {
    if (n == 0) return 0;
    int digit = n % 10;
    return power_recursive(digit, numDigits) + armstrong_sum(n / 10, numDigits);
}

int main() {
    int n;
    cin >> n;

    // Count number of digits
    int numDigits = 0, temp = n;
    while (temp > 0) {
        temp /= 10;
        numDigits++;
    }

    // Calculate Armstrong sum
    int sum = armstrong_sum(n, numDigits);

    // Check if Armstrong number
    if (sum == n) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}