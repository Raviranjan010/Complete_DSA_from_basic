# Primes, Sieve of Eratosthenes & Prime Factorization

**Phase:** Phase 2 — Math for DSA | **Prerequisites:** [00-Start-Here/concepts/07-conditionals-and-loops.md](../../00-Start-Here/concepts/07-conditionals-and-loops.md)
**Difficulty to grasp:** Intermediate
**Pattern tag(s):** `#math`, `#primes`, `#sieve`, `#number-theory`

---

## 1. Why This Matters (Motivation)
Prime numbers are the multiplicative building blocks of all integers (Fundamental Theorem of Arithmetic). Fast prime checking and generation are essential for hashing, cryptography, randomized algorithms, and combinatorial counting.

---

## 2. Intuition & Sieve Mechanics
Testing each number up to $N$ individually takes $\mathcal{O}(N \sqrt{N})$ time.
Instead of testing each number, the **Sieve of Eratosthenes** works backward: start with all numbers marked as prime, and iteratively cross off multiples of each identified prime.

```text
Numbers from 2 to 25:
Prime 2: Mark 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24
Prime 3: Mark 9, 12, 15, 18, 21, 24 (Start from 3*3 = 9!)
Prime 5: Mark 25 (Start from 5*5 = 25!)
All unmarked numbers {2, 3, 5, 7, 11, 13, 17, 19, 23} are primes!
```

---

## 3. C++17 Implementation
```cpp
#include <iostream>
#include <vector>

// Sieve of Eratosthenes: O(N log log N)
std::vector<bool> sieve(int n) {
    std::vector<bool> isPrime(n + 1, true);
    isPrime[0] = isPrime[1] = false;

    for (int p = 2; p * p <= n; ++p) {
        if (isPrime[p]) {
            for (int i = p * p; i <= n; i += p) {
                isPrime[i] = false;
            }
        }
    }
    return isPrime;
}

// Smallest Prime Factor (SPF) for O(log N) queries
std::vector<int> computeSPF(int n) {
    std::vector<int> spf(n + 1);
    for (int i = 0; i <= n; ++i) spf[i] = i;

    for (int p = 2; p * p <= n; ++p) {
        if (spf[p] == p) {
            for (int i = p * p; i <= n; i += p) {
                if (spf[i] == i) spf[i] = p;
            }
        }
    }
    return spf;
}

std::vector<int> getFactorization(int x, const std::vector<int>& spf) {
    std::vector<int> factors;
    while (x > 1) {
        factors.push_back(spf[x]);
        x /= spf[x];
    }
    return factors;
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
```

---

## 4. Complexity Analysis
- **Sieve Time Complexity:** $\mathcal{O}(N \sum_{p \le N} \frac{1}{p}) = \mathcal{O}(N \log \log N)$.
- **Prime Factorization with SPF:** Precomputation $\mathcal{O}(N \log \log N)$; per-query factorization $\mathcal{O}(\log X)$.
- **Space Complexity:** $\mathcal{O}(N)$ boolean / integer table.
