#include <iostream>
#include <vector>

std::vector<bool> sieve(int n) {
    std::vector<bool> isPrime(n + 1, true);
    if (n >= 0) isPrime[0] = false;
    if (n >= 1) isPrime[1] = false;

    for (int p = 2; p * p <= n; ++p) {
        if (isPrime[p]) {
            for (int i = p * p; i <= n; i += p) {
                isPrime[i] = false;
            }
        }
    }
    return isPrime;
}

int main() {
    int limit = 30;
    auto isPrime = sieve(limit);
    std::cout << "Primes up to " << limit << ":\n";
    for (int i = 2; i <= limit; ++i) {
        if (isPrime[i]) std::cout << i << " ";
    }
    std::cout << "\n";
    return 0;
}
