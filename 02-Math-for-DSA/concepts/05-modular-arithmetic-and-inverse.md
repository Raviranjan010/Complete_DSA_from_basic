# Modular Arithmetic, Fast Powers & Modular Inverse

**Phase:** Phase 2 — Math for DSA | **Prerequisites:** [01-gcd-and-euclidean-algorithm.md](01-gcd-and-euclidean-algorithm.md)
**Difficulty to grasp:** Intermediate
**Pattern tag(s):** `#math`, `#modular-arithmetic`, `#fermat-little-theorem`

---

## 1. Why This Matters (Motivation)
In competitive programming and combinatorics, answer values often grow exponentially (e.g. permutations $N!$, paths on a grid). Platforms ask for results modulo a large prime $M = 10^9 + 7$ or $998244353$ to prevent overflow while testing algorithmic correctness.

---

## 2. Core Rules of Modular Arithmetic
1. **Addition:** $(a + b) \pmod M = ((a \pmod M) + (b \pmod M)) \pmod M$
2. **Subtraction:** $(a - b) \pmod M = ((a \pmod M) - (b \pmod M) + M) \pmod M$ (Note the $+ M$ to prevent negative remainders in C++/Java!)
3. **Multiplication:** $(a \times b) \pmod M = ((a \pmod M) \times (b \pmod M)) \pmod M$
4. **Division:** $(a / b) \pmod M \neq ((a \pmod M) / (b \pmod M)) \pmod M$. Instead, $(a / b) \pmod M = (a \times b^{-1}) \pmod M$, where $b^{-1}$ is the **modular multiplicative inverse**.

---

## 3. Modular Inverse via Fermat's Little Theorem
When the modulus $M$ is prime and $\gcd(b, M) = 1$:
$$b^{M-1} \equiv 1 \pmod M \implies b \times b^{M-2} \equiv 1 \pmod M$$
Therefore, the modular inverse of $b$ modulo $M$ is:
$$b^{-1} \equiv b^{M-2} \pmod M$$
Computed in $\mathcal{O}(\log M)$ using fast binary exponentiation.

---

## 4. C++17 Implementation
```cpp
#include <iostream>

const long long MOD = 1e9 + 7;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (__int128(res) * base) % MOD;
        base = (__int128(base) * base) % MOD;
        exp /= 2;
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
```

---

## 5. Complexity Analysis
- **Time Complexity:** $\mathcal{O}(\log M)$ for computing modular inverse and binary exponentiation.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary memory.
