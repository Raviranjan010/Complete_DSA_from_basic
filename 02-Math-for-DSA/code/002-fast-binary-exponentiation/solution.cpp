#include <iostream>

long long power(long long base, long long exp, long long mod = 1e9 + 7) {
    long long res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = (__int128(res) * base) % mod;
        base = (__int128(base) * base) % mod;
        exp >>= 1;
    }
    return res;
}

int main() {
    long long base = 2, exp = 10;
    std::cout << base << "^" << exp << " mod 1e9+7 = " << power(base, exp) << "\n";
    return 0;
}
