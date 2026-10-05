# Module 02: Math for DSA — Number Theory, Modular Arithmetic & Primality

[← Back to Root Roadmap](../README.md) · [Next Module: 03 Arrays & Strings →](../03-Arrays-and-Strings/README.md) · [Cheatsheet: C++ Core Syntax](../20-Cheatsheets/cpp-stl-cheatsheet.md)

---

## 1. What This Module Is & Why It Matters
Algorithms and mathematics are fundamentally inseparable. A vast range of computational problems—from hashing algorithms and cryptographic protocols to competitive programming challenges—rely on fast number theoretic primitives.

This module delivers full mastery of discrete math algorithms: GCD via the Euclidean algorithm, fast binary exponentiation, prime sieves, prime factorization using smallest prime factors, and modular arithmetic including modular inverses.

### Core Objectives
1. **Master Euclid's Algorithm:** Compute greatest common divisors and least common multiples in $\mathcal{O}(\log(\min(a, b)))$ time.
2. **Exponential Speedup via Binary Exponentiation:** Calculate $A^B \pmod M$ in $\mathcal{O}(\log B)$ steps rather than linear $\mathcal{O}(B)$ iteration.
3. **Prime Generation & Sieves:** Generate all primes up to $N$ in $\mathcal{O}(N \log \log N)$ and factorize queries in $\mathcal{O}(\log X)$ using precomputed SPF arrays.
4. **Master Modular Arithmetic:** Perform addition, subtraction, multiplication, and division under modulo $10^9 + 7$ without integer overflow bugs.

---

## 2. Recommended Study Order

```text
+------------------------------------------+
| 01. Greatest Common Divisor & LCM        | -> Read: 01-gcd-and-euclidean-algorithm.md
|                                          |    Problem: 001-gcd-and-lcm-euclidean
+------------------------------------------+
                     |
                     v
+------------------------------------------+
| 02. Digit Mathematics & Narcissistic     | -> Read: 03-armstrong-and-digit-math.md
|                                          |    Problem: 006-armstrong-and-palindrome-number
+------------------------------------------+
                     |
                     v
+------------------------------------------+
| 03. Fast Binary Exponentiation           | -> Read: 02-fast-exponentiation-and-powers.md
|                                          |    Problem: 002-fast-binary-exponentiation
+------------------------------------------+
                     |
                     v
+------------------------------------------+
| 04. Primes & Sieve of Eratosthenes       | -> Read: 04-sieve-of-eratosthenes-and-primes.md
|                                          |    Problem: 003-sieve-of-eratosthenes
|                                          |    Problem: 004-prime-factorization-spf
+------------------------------------------+
                     |
                     v
+------------------------------------------+
| 05. Modular Arithmetic & Inverse         | -> Read: 05-modular-arithmetic-and-inverse.md
|                                          |    Problem: 005-modular-arithmetic-and-inverse
+------------------------------------------+
```

---

## 3. Concept Guides Directory

| # | Concept Guide | Core Topics Covered | Read Time |
|---|---|---|---|
| 01 | [GCD & Euclidean Algorithm](concepts/01-gcd-and-euclidean-algorithm.md) | Division algorithm, Lamé's theorem, safe LCM calculation | 15 min |
| 02 | [Fast Exponentiation & Powers](concepts/02-fast-exponentiation-and-powers.md) | Repeated squaring, modular exponentiation, negative powers | 20 min |
| 03 | [Armstrong & Digit Math](concepts/03-armstrong-and-digit-math.md) | Base-10 modulo/division, integer reversal, overflow protection | 15 min |
| 04 | [Sieve of Eratosthenes & Primes](concepts/04-sieve-of-eratosthenes-and-primes.md) | Prime checking $\mathcal{O}(\sqrt{N})$, Sieve $\mathcal{O}(N \log \log N)$, SPF | 25 min |
| 05 | [Modular Arithmetic & Inverse](concepts/05-modular-arithmetic-and-inverse.md) | Modulo rules, negative modulo handling, Fermat's Little Theorem | 20 min |

---

## 4. Problem & Code Portfolio

| # | Problem Name | Difficulty | Tier | Key Patterns | Solutions | Reference Link |
|---|---|---|---|---|---|---|
| 001 | [GCD and LCM Euclidean](problems/001-gcd-and-lcm-euclidean.md) | 🟢 Easy | Tier A | `#math`, `#euclidean-algorithm` | [C++17](code/001-gcd-and-lcm-euclidean/solution.cpp) · [Python3](code/001-gcd-and-lcm-euclidean/solution.py) · [Java17](code/001-gcd-and-lcm-euclidean/Solution.java) | [LeetCode 1979](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) |
| 002 | [Fast Binary Exponentiation](problems/002-fast-binary-exponentiation.md) | 🟡 Medium | Tier A | `#math`, `#binary-exponentiation` | [C++17](code/002-fast-binary-exponentiation/solution.cpp) · [Python3](code/002-fast-binary-exponentiation/solution.py) · [Java17](code/002-fast-binary-exponentiation/Solution.java) | [LeetCode 50](https://leetcode.com/problems/powx-n/) |
| 003 | [Sieve of Eratosthenes](problems/003-sieve-of-eratosthenes.md) | 🟡 Medium | Tier A | `#math`, `#sieve`, `#primes` | [C++17](code/003-sieve-of-eratosthenes/solution.cpp) · [Python3](code/003-sieve-of-eratosthenes/solution.py) · [Java17](code/003-sieve-of-eratosthenes/Solution.java) | [LeetCode 204](https://leetcode.com/problems/count-primes/) |
| 004 | [Prime Factorization SPF](problems/004-prime-factorization-spf.md) | 🟡 Medium | Tier A | `#math`, `#spf`, `#factorization` | [C++17](code/004-prime-factorization-spf/solution.cpp) · [Python3](code/004-prime-factorization-spf/solution.py) · [Java17](code/004-prime-factorization-spf/Solution.java) | [GeeksforGeeks](https://www.geeksforgeeks.org/prime-factorization-using-sieve-olog-n-multiple-queries/) |
| 005 | [Modular Arithmetic & Inverse](problems/005-modular-arithmetic-and-inverse.md) | 🟡 Medium | Tier A | `#math`, `#modular-arithmetic` | [C++17](code/005-modular-arithmetic-and-inverse/solution.cpp) · [Python3](code/005-modular-arithmetic-and-inverse/solution.py) · [Java17](code/005-modular-arithmetic-and-inverse/Solution.java) | [GeeksforGeeks](https://www.geeksforgeeks.org/modular-division/) |
| 006 | [Armstrong & Palindrome Number](problems/006-armstrong-and-palindrome-number.md) | 🟢 Easy | Tier A | `#math`, `#digit-manipulation` | [C++17](code/006-armstrong-and-palindrome-number/solution.cpp) · [Python3](code/006-armstrong-and-palindrome-number/solution.py) · [Java17](code/006-armstrong-and-palindrome-number/Solution.java) | [LeetCode 9](https://leetcode.com/problems/palindrome-number/) |

---

## 5. Top 5 Interview Pitfalls & Common Bugs
1. **Integer Overflow During LCM Multiplication:** Computing `(a * b) / gcd` overflows a 64-bit integer if $a \times b > 2^{63}-1$. Always compute `(a / gcd) * b`.
2. **Negative Modulo in C++ and Java:** In C++ and Java, `-5 % 3` evaluates to `-2` (not `1`). When taking modulo of a difference, always add the modulus: `(a - b) % M + M) % M`.
3. **Sieve Array Index Out-of-Bounds:** When marking multiples in the sieve starting at $p^2$, ensure $p \times p$ does not overflow 32-bit signed integers (e.g. when $p \approx 50,000$, $p^2 \approx 2.5 \times 10^9 > \text{INT\_MAX}$). Use `long long` for loop counters: `for (long long i = (long long)p * p; i <= n; i += p)`.
4. **Dividing Under Modulo Directly:** Never write `(a / b) % M`! Modular division requires multiplying by the modular multiplicative inverse: `(a * modInverse(b)) % M`.
5. **Reversing Integers Without Overflow Guard:** Reversing $1,534,236,469$ produces an integer that overflows 32-bit signed storage. Check boundary conditions before multiplying by 10.

---

## 6. What's Next
Now that you possess the mathematical foundation of number theory and complexity analysis, step into fundamental linear data structures:
👉 **[Module 03: Arrays & Strings (Traversal, Dynamic Sizing, Kadane's Algorithm, Subarrays)](../03-Arrays-and-Strings/README.md)**
