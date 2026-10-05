#include <iostream>

const long long MOD = 1e9 + 7;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (__int128(res) * base) % MOD;
        base = (__int128(base) * base) % MOD;
        exp >>= 1;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

long long modDivide(long long a, long long b) {
    return (a % MOD * modInverse(b)) % MOD;
}

int main() {
    long long a = 14, b = 2;
    std::cout << a << " / " << b << " mod " << MOD << " = " << modDivide(a, b) << "\n";
    return 0;
}
