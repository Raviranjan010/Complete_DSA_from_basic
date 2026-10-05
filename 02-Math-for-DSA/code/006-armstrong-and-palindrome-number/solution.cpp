#include <iostream>
#include <cmath>

bool isArmstrong(long long n) {
    if (n < 0) return false;
    long long temp = n;
    int k = 0;
    while (temp > 0) {
        k++;
        temp /= 10;
    }
    long long sum = 0;
    temp = n;
    while (temp > 0) {
        long long d = temp % 10;
        sum += std::pow(d, k);
        temp /= 10;
    }
    return sum == n;
}

bool isPalindrome(int x) {
    if (x < 0 || (x % 10 == 0 && x != 0)) return false;
    int revertedNumber = 0;
    while (x > revertedNumber) {
        revertedNumber = revertedNumber * 10 + x % 10;
        x /= 10;
    }
    return x == revertedNumber || x == revertedNumber / 10;
}

int main() {
    long long n = 153;
    std::cout << n << " is Armstrong? " << (isArmstrong(n) ? "Yes" : "No") << "\n";
    int p = 1221;
    std::cout << p << " is Palindrome? " << (isPalindrome(p) ? "Yes" : "No") << "\n";
    return 0;
}
