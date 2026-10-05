# Greatest Common Divisor (GCD) & Euclidean Algorithm

**Phase:** Phase 2 — Math for DSA | **Prerequisites:** [00-Start-Here/concepts/03-cpp-fundamentals.md](../../00-Start-Here/concepts/03-cpp-fundamentals.md)
**Difficulty to grasp:** Beginner
**Pattern tag(s):** `#math`, `#number-theory`, `#euclidean-algorithm`

---

## 1. Why This Matters (Motivation)
The Greatest Common Divisor ($\gcd$) of two integers is the largest positive integer that divides both without a remainder. It is the cornerstone of number theory in computer science: simplifying fractions, calculating Lowest Common Multiples ($\text{lcm}$), computing modular inverses in cryptography (RSA), and solving Diophantine equations.

---

## 2. Intuition First
Consider two measuring rods of length $A = 48$ and $B = 18$. We want the longest possible ruler that can measure both rods exactly without fractions.
If a ruler of length $g$ measures both $48$ and $18$, it must also measure their difference: $48 - 18 = 30$, and $30 - 18 = 12$, and $18 - 12 = 6$, and $12 - 6 = 6$.
When both lengths become equal to $6$, the longest ruler is $6$!
Instead of repeated subtractions, we take the remainder: $48 \pmod{18} = 12$.

```text
Step 1: gcd(48, 18) -> 48 = 18 * 2 + 12 -> next: gcd(18, 12)
Step 2: gcd(18, 12) -> 18 = 12 * 1 + 6  -> next: gcd(12, 6)
Step 3: gcd(12, 6)  -> 12 = 6 * 2 + 0   -> next: gcd(6, 0)
Step 4: gcd(6, 0)   -> remainder is 0! Result = 6.
```

---

## 3. Formal Explanation
Euclid's algorithm relies on the theorem:
$$\gcd(a, b) = \begin{cases} a & \text{if } b = 0 \\ \gcd(b, a \pmod b) & \text{if } b > 0 \end{cases}$$

### Relation to Lowest Common Multiple (LCM)
For any two positive integers $a$ and $b$:
$$a \times b = \gcd(a, b) \times \text{lcm}(a, b) \implies \text{lcm}(a, b) = \frac{a \times b}{\gcd(a, b)}$$
To prevent integer overflow in code, always divide before multiplying:
$$\text{lcm}(a, b) = \left(\frac{a}{\gcd(a, b)}\right) \times b$$

---

## 4. Step-by-Step Dry Run
Let $a = 252, b = 105$:
1. $252 \pmod{105} = 42 \implies \gcd(105, 42)$
2. $105 \pmod{42} = 21 \implies \gcd(42, 21)$
3. $42 \pmod{21} = 0 \implies \gcd(21, 0)$
4. $b = 0 \implies \text{return } 21$.

Total steps: 3.

---

## 5. C++17 Implementation
```cpp
#include <iostream>
#include <numeric>

// Iterative Euclidean Algorithm: O(1) space
long long computeGcd(long long a, long long b) {
    while (b != 0) {
        long long remainder = a % b;
        a = b;
        b = remainder;
    }
    return a;
}

// Safe LCM to prevent overflow
long long computeLcm(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / computeGcd(a, b)) * b;
}

int main() {
    long long a = 48, b = 18;
    std::cout << "GCD(" << a << ", " << b << ") = " << computeGcd(a, b) << "\n";
    std::cout << "LCM(" << a << ", " << b << ") = " << computeLcm(a, b) << "\n";
    std::cout << "std::gcd: " << std::gcd(a, b) << "\n";
    return 0;
}
```

---

## 6. Complexity Analysis
- **Time Complexity:** $\mathcal{O}(\log(\min(a, b)))$. By Lamé's Theorem, the worst-case scenario occurs when $a$ and $b$ are consecutive Fibonacci numbers ($F_{k+1}, F_k$), taking at most $5 \times \text{digits}(b)$ steps.
- **Space Complexity:** $\mathcal{O}(1)$ for iterative implementation; $\mathcal{O}(\log(\min(a, b)))$ for recursive call stack.

---

## 7. Common Mistakes & Edge Cases
1. **Handling Zero:** $\gcd(a, 0) = |a|$. $\gcd(0, 0)$ is undefined (or treated as $0$ by convention).
2. **Negative Numbers:** In C++, `(-7) % 3` yields `-1`. Standard mathematical $\gcd$ is strictly positive. Always apply `std::abs()` to inputs.
3. **LCM Overflow:** Writing `(a * b) / gcd(a, b)` can overflow a 32-bit or 64-bit integer even if the final result fits! Always divide first: `(a / gcd(a, b)) * b`.

---

## 8. How This Shows up in Interviews
- Interviewers test whether you calculate GCD iteratively in $\mathcal{O}(\log(\min(a, b)))$ instead of a brute-force $\mathcal{O}(\min(a, b))$ loop.
- Key variants: Extended Euclidean Algorithm (finding $x, y$ such that $ax + by = \gcd(a, b)$) and modular inverse.

---

## 9. What's Next
Proceed to fast exponentiation to compute large powers and modular inverses in $\mathcal{O}(\log P)$ time:
👉 **[02 Fast Exponentiation and Powers](02-fast-exponentiation-and-powers.md)**
