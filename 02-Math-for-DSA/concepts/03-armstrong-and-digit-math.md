# Digit Manipulation, Armstrong Numbers & Numeric Reversal

**Phase:** Phase 2 — Math for DSA | **Prerequisites:** [00-Start-Here/concepts/07-conditionals-and-loops.md](../../00-Start-Here/concepts/07-conditionals-and-loops.md)
**Difficulty to grasp:** Beginner
**Pattern tag(s):** `#math`, `#digit-manipulation`

---

## 1. Why This Matters (Motivation)
Fundamental numeric interview questions (reversing integers, checking palindromes, counting digits, summing digits) all boil down to extracting digits using base-10 modulo (`% 10`) and division (`/ 10`). Mastering digit decomposition without converting numbers to strings is critical for $\mathcal{O}(1)$ space performance and avoiding integer overflow bugs.

---

## 2. Intuition & Digit Extraction Pattern
In any base $B$ positional number system:
- The least significant digit is obtained with: `digit = n % 10`
- The remaining prefix of the number is obtained with: `n = n / 10`
- Appending a digit $d$ to a reversed accumulator: `rev = rev * 10 + d`

```text
Processing n = 153:
Iteration 1: digit = 153 % 10 = 3 | n = 153 / 10 = 15 | rev = 0 * 10 + 3 = 3
Iteration 2: digit = 15 % 10 = 5  | n = 15 / 10 = 1   | rev = 3 * 10 + 5 = 35
Iteration 3: digit = 1 % 10 = 1   | n = 1 / 10 = 0    | rev = 35 * 10 + 1 = 351
Terminates when n == 0.
```

---

## 3. Armstrong (Narcissistic) Numbers
A positive integer $N$ with $K$ digits is an **Armstrong number** if the sum of each digit raised to the power $K$ equals $N$:
$$N = \sum_{i=1}^K d_i^K$$
For example, for $153$ ($K = 3$ digits):
$$1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 \quad \text{(Armstrong Number)}$$

---

## 4. C++17 Implementation
```cpp
#include <iostream>
#include <cmath>
#include <climits>

// Check Armstrong number
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

// Reverse integer safely with overflow check (LeetCode 7)
int reverseIntegerSafely(int x) {
    int rev = 0;
    while (x != 0) {
        int pop = x % 10;
        x /= 10;
        
        // Overflow check before multiplying by 10
        if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
        if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
        
        rev = rev * 10 + pop;
    }
    return rev;
}

int main() {
    long long num = 153;
    std::cout << num << " is Armstrong? " << (isArmstrong(num) ? "Yes" : "No") << "\n";
    std::cout << "Reversed 12345: " << reverseIntegerSafely(12345) << "\n";
    return 0;
}
```

---

## 5. Complexity Analysis
- **Time Complexity:** $\mathcal{O}(\log_{10} N)$ operations, since the number of digits in $N$ is $\lfloor \log_{10} N \rfloor + 1$.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

---

## 6. Common Mistakes & Edge Cases
1. **Integer Overflow on Reversal:** Reversing a 32-bit integer like `1,999,999,999` results in a number that exceeds `INT_MAX` ($2,147,483,647$). You must check boundaries before `rev = rev * 10 + pop`.
2. **Negative Numbers:** Palindrome numbers are generally defined as false for negative integers because the minus sign `-` does not match the trailing digit.
