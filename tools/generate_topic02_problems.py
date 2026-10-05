import os
import shutil

base_dir = "02-Math-for-DSA"
code_dir = os.path.join(base_dir, "code")
prob_dir = os.path.join(base_dir, "problems")
os.makedirs(code_dir, exist_ok=True)
os.makedirs(prob_dir, exist_ok=True)

# Problem 1: GCD and LCM Euclidean
p1_code = os.path.join(code_dir, "001-gcd-and-lcm-euclidean")
os.makedirs(p1_code, exist_ok=True)

with open(os.path.join(p1_code, "solution.cpp"), "w", encoding="utf-8") as f:
    f.write('''#include <iostream>
#include <numeric>

long long computeGcd(long long a, long long b) {
    while (b != 0) {
        long long rem = a % b;
        a = b;
        b = rem;
    }
    return a;
}

long long computeLcm(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / computeGcd(a, b)) * b;
}

int main() {
    long long a = 48, b = 18;
    std::cout << "GCD(" << a << ", " << b << ") = " << computeGcd(a, b) << "\\n";
    std::cout << "LCM(" << a << ", " << b << ") = " << computeLcm(a, b) << "\\n";
    return 0;
}
''')

with open(os.path.join(p1_code, "solution.py"), "w", encoding="utf-8") as f:
    f.write('''import math

def compute_gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def compute_lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return (a // compute_gcd(a, b)) * b

if __name__ == "__main__":
    a, b = 48, 18
    print(f"GCD({a}, {b}) = {compute_gcd(a, b)}")
    print(f"LCM({a}, {b}) = {compute_lcm(a, b)}")
''')

with open(os.path.join(p1_code, "Solution.java"), "w", encoding="utf-8") as f:
    f.write('''public class Solution {
    public static long computeGcd(long a, long b) {
        while (b != 0) {
            long rem = a % b;
            a = b;
            b = rem;
        }
        return a;
    }

    public static long computeLcm(long a, long b) {
        if (a == 0 || b == 0) return 0;
        return (a / computeGcd(a, b)) * b;
    }

    public static void main(String[] args) {
        long a = 48, b = 18;
        System.out.println("GCD(" + a + ", " + b + ") = " + computeGcd(a, b));
        System.out.println("LCM(" + a + ", " + b + ") = " + computeLcm(a, b));
    }
}
''')

with open(os.path.join(prob_dir, "001-gcd-and-lcm-euclidean.md"), "w", encoding="utf-8") as f:
    f.write('''# Greatest Common Divisor (GCD) and Lowest Common Multiple (LCM)

[← Back to Module Overview](../README.md) · [Concepts: GCD & Euclidean Algorithm](../concepts/01-gcd-and-euclidean-algorithm.md)

---

## 1. Problem Overview
- **Name:** Greatest Common Divisor and Lowest Common Multiple
- **Difficulty:** Easy
- **Tier:** A (Flagship Foundation)
- **Pattern:** `#math`, `#euclidean-algorithm`, `#number-theory`
- **External Links:** [LeetCode 1979: Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) · [GeeksforGeeks: GCD and LCM](https://www.geeksforgeeks.org/program-to-find-gcd-or-hcf-of-two-numbers/)

---

## 2. Problem Statement
Given two positive integers $a$ and $b$, compute their Greatest Common Divisor ($\gcd$) and Lowest Common Multiple ($\text{lcm}$) using Euclid's algorithm in $\mathcal{O}(\log(\min(a, b)))$ time and $\mathcal{O}(1)$ auxiliary space.

---

## 3. Complexity Analysis
- **Time Complexity:** $\mathcal{O}(\log(\min(a, b)))$
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary memory
''')

# Problem 2: Fast Binary Exponentiation
p2_code = os.path.join(code_dir, "002-fast-binary-exponentiation")
os.makedirs(p2_code, exist_ok=True)

with open(os.path.join(p2_code, "solution.cpp"), "w", encoding="utf-8") as f:
    f.write('''#include <iostream>

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
    std::cout << base << "^" << exp << " mod 1e9+7 = " << power(base, exp) << "\\n";
    return 0;
}
''')

with open(os.path.join(p2_code, "solution.py"), "w", encoding="utf-8") as f:
    f.write('''def power(base: int, exp: int, mod: int = 10**9 + 7) -> int:
    res = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return res

if __name__ == "__main__":
    print(f"2^10 mod 1e9+7 = {power(2, 10)}")
''')

with open(os.path.join(p2_code, "Solution.java"), "w", encoding="utf-8") as f:
    f.write('''public class Solution {
    public static long power(long base, long exp, long mod) {
        long res = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return res;
    }

    public static void main(String[] args) {
        long mod = 1000000007L;
        System.out.println("2^10 mod 1e9+7 = " + power(2, 10, mod));
    }
}
''')

with open(os.path.join(prob_dir, "002-fast-binary-exponentiation.md"), "w", encoding="utf-8") as f:
    f.write('''# Fast Binary Exponentiation (Pow(x, n))

[← Back to Module Overview](../README.md) · [Concepts: Fast Exponentiation](../concepts/02-fast-exponentiation-and-powers.md)

---

## 1. Problem Overview
- **Name:** Modular Binary Exponentiation
- **Difficulty:** Medium
- **Tier:** A (Flagship Foundation)
- **Pattern:** `#math`, `#binary-exponentiation`, `#divide-and-conquer`
- **External Links:** [LeetCode 50: Pow(x, n)](https://leetcode.com/problems/powx-n/) · [GeeksforGeeks: Modular Exponentiation](https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/)

---

## 2. Problem Statement
Compute $A^B \pmod M$ in $\mathcal{O}(\log B)$ time, where $B$ can be up to $10^{18}$.

---

## 3. Complexity Analysis
- **Time Complexity:** $\mathcal{O}(\log B)$
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary memory
''')

# Problem 3: Sieve of Eratosthenes
p3_code = os.path.join(code_dir, "003-sieve-of-eratosthenes")
os.makedirs(p3_code, exist_ok=True)

with open(os.path.join(p3_code, "solution.cpp"), "w", encoding="utf-8") as f:
    f.write('''#include <iostream>
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
    std::cout << "Primes up to " << limit << ":\\n";
    for (int i = 2; i <= limit; ++i) {
        if (isPrime[i]) std::cout << i << " ";
    }
    std::cout << "\\n";
    return 0;
}
''')

with open(os.path.join(p3_code, "solution.py"), "w", encoding="utf-8") as f:
    f.write('''def sieve(n: int) -> list[bool]:
    if n < 2:
        return [False] * (n + 1)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime

if __name__ == "__main__":
    limit = 30
    primes = sieve(limit)
    print("Primes up to 30:", [i for i in range(2, limit + 1) if primes[i]])
''')

with open(os.path.join(p3_code, "Solution.java"), "w", encoding="utf-8") as f:
    f.write('''import java.util.Arrays;

public class Solution {
    public static boolean[] sieve(int n) {
        boolean[] isPrime = new boolean[n + 1];
        Arrays.fill(isPrime, true);
        if (n >= 0) isPrime[0] = false;
        if (n >= 1) isPrime[1] = false;

        for (int p = 2; p * p <= n; p++) {
            if (isPrime[p]) {
                for (int i = p * p; i <= n; i += p) {
                    isPrime[i] = false;
                }
            }
        }
        return isPrime;
    }

    public static void main(String[] args) {
        int limit = 30;
        boolean[] primes = sieve(limit);
        System.out.print("Primes up to " + limit + ": ");
        for (int i = 2; i <= limit; i++) {
            if (primes[i]) System.out.print(i + " ");
        }
        System.out.println();
    }
}
''')

with open(os.path.join(prob_dir, "003-sieve-of-eratosthenes.md"), "w", encoding="utf-8") as f:
    f.write('''# Sieve of Eratosthenes & Prime Generation

[← Back to Module Overview](../README.md) · [Concepts: Sieve & Primes](../concepts/04-sieve-of-eratosthenes-and-primes.md)

---

## 1. Problem Overview
- **Name:** Sieve of Eratosthenes Prime Generation
- **Difficulty:** Medium
- **Tier:** A (Flagship Foundation)
- **Pattern:** `#math`, `#sieve`, `#primes`
- **External Links:** [LeetCode 204: Count Primes](https://leetcode.com/problems/count-primes/) · [GeeksforGeeks: Sieve of Eratosthenes](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)

---

## 2. Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N \log \log N)$
- **Space Complexity:** $\mathcal{O}(N)$ boolean vector
''')

# Problem 4: Prime Factorization SPF
p4_code = os.path.join(code_dir, "004-prime-factorization-spf")
os.makedirs(p4_code, exist_ok=True)

with open(os.path.join(p4_code, "solution.cpp"), "w", encoding="utf-8") as f:
    f.write('''#include <iostream>
#include <vector>

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

std::vector<int> factorize(int x, const std::vector<int>& spf) {
    std::vector<int> factors;
    while (x > 1) {
        factors.push_back(spf[x]);
        x /= spf[x];
    }
    return factors;
}

int main() {
    int maxLimit = 100;
    auto spf = computeSPF(maxLimit);
    int num = 84;
    auto factors = factorize(num, spf);
    std::cout << "Prime factors of " << num << ": ";
    for (int f : factors) std::cout << f << " ";
    std::cout << "\\n";
    return 0;
}
''')

with open(os.path.join(p4_code, "solution.py"), "w", encoding="utf-8") as f:
    f.write('''def compute_spf(n: int) -> list[int]:
    spf = list(range(n + 1))
    p = 2
    while p * p <= n:
        if spf[p] == p:
            for i in range(p * p, n + 1, p):
                if spf[i] == i:
                    spf[i] = p
        p += 1
    return spf

def factorize(x: int, spf: list[int]) -> list[int]:
    factors = []
    while x > 1:
        factors.append(spf[x])
        x //= spf[x]
    return factors

if __name__ == "__main__":
    spf = compute_spf(100)
    print("Prime factors of 84:", factorize(84, spf))
''')

with open(os.path.join(p4_code, "Solution.java"), "w", encoding="utf-8") as f:
    f.write('''import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static int[] computeSPF(int n) {
        int[] spf = new int[n + 1];
        for (int i = 0; i <= n; i++) spf[i] = i;

        for (int p = 2; p * p <= n; p++) {
            if (spf[p] == p) {
                for (int i = p * p; i <= n; i += p) {
                    if (spf[i] == i) spf[i] = p;
                }
            }
        }
        return spf;
    }

    public static List<Integer> factorize(int x, int[] spf) {
        List<Integer> factors = new ArrayList<>();
        while (x > 1) {
            factors.add(spf[x]);
            x /= spf[x];
        }
        return factors;
    }

    public static void main(String[] args) {
        int[] spf = computeSPF(100);
        System.out.println("Prime factors of 84: " + factorize(84, spf));
    }
}
''')

with open(os.path.join(prob_dir, "004-prime-factorization-spf.md"), "w", encoding="utf-8") as f:
    f.write('''# Prime Factorization in O(log N) using Smallest Prime Factor (SPF)

[← Back to Module Overview](../README.md) · [Concepts: Sieve & Primes](../concepts/04-sieve-of-eratosthenes-and-primes.md)

---

## 1. Problem Overview
- **Name:** Fast Prime Factorization via Smallest Prime Factor
- **Difficulty:** Medium
- **Tier:** A (Flagship Foundation)
- **Pattern:** `#math`, `#spf`, `#prime-factorization`
- **External Links:** [GeeksforGeeks: Prime Factorization using Sieve](https://www.geeksforgeeks.org/prime-factorization-using-sieve-olog-n-multiple-queries/)

---

## 2. Complexity Analysis
- **Precomputation:** $\mathcal{O}(N \log \log N)$
- **Query Time:** $\mathcal{O}(\log X)$
- **Space Complexity:** $\mathcal{O}(N)$ integer array
''')

# Problem 5: Modular Arithmetic & Inverse
p5_code = os.path.join(code_dir, "005-modular-arithmetic-and-inverse")
os.makedirs(p5_code, exist_ok=True)

with open(os.path.join(p5_code, "solution.cpp"), "w", encoding="utf-8") as f:
    f.write('''#include <iostream>

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
    std::cout << a << " / " << b << " mod " << MOD << " = " << modDivide(a, b) << "\\n";
    return 0;
}
''')

with open(os.path.join(p5_code, "solution.py"), "w", encoding="utf-8") as f:
    f.write('''MOD = 10**9 + 7

def power(base: int, exp: int) -> int:
    return pow(base, exp, MOD)

def mod_inverse(n: int) -> int:
    return power(n, MOD - 2)

def mod_divide(a: int, b: int) -> int:
    return (a % MOD * mod_inverse(b)) % MOD

if __name__ == "__main__":
    print(f"14 / 2 mod 1e9+7 = {mod_divide(14, 2)}")
''')

with open(os.path.join(p5_code, "Solution.java"), "w", encoding="utf-8") as f:
    f.write('''public class Solution {
    static final long MOD = 1000000007L;

    public static long power(long base, long exp) {
        long res = 1;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return res;
    }

    public static long modInverse(long n) {
        return power(n, MOD - 2);
    }

    public static long modDivide(long a, long b) {
        return (a % MOD * modInverse(b)) % MOD;
    }

    public static void main(String[] args) {
        System.out.println("14 / 2 mod 1e9+7 = " + modDivide(14, 2));
    }
}
''')

with open(os.path.join(prob_dir, "005-modular-arithmetic-and-inverse.md"), "w", encoding="utf-8") as f:
    f.write('''# Modular Arithmetic Operations & Fermat's Modular Inverse

[← Back to Module Overview](../README.md) · [Concepts: Modular Arithmetic](../concepts/05-modular-arithmetic-and-inverse.md)

---

## 1. Problem Overview
- **Name:** Modular Arithmetic & Multiplicative Inverse
- **Difficulty:** Medium
- **Tier:** A (Flagship Foundation)
- **Pattern:** `#math`, `#modular-arithmetic`, `#fermat-little-theorem`
- **External Links:** [GeeksforGeeks: Modular Division](https://www.geeksforgeeks.org/modular-division/)

---

## 2. Complexity Analysis
- **Time Complexity:** $\mathcal{O}(\log M)$
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space
''')

# Problem 6: Armstrong & Palindrome Number
p6_code = os.path.join(code_dir, "006-armstrong-and-palindrome-number")
os.makedirs(p6_code, exist_ok=True)

with open(os.path.join(p6_code, "solution.cpp"), "w", encoding="utf-8") as f:
    f.write('''#include <iostream>
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
    std::cout << n << " is Armstrong? " << (isArmstrong(n) ? "Yes" : "No") << "\\n";
    int p = 1221;
    std::cout << p << " is Palindrome? " << (isPalindrome(p) ? "Yes" : "No") << "\\n";
    return 0;
}
''')

with open(os.path.join(p6_code, "solution.py"), "w", encoding="utf-8") as f:
    f.write('''def is_armstrong(n: int) -> bool:
    if n < 0:
        return False
    digits = [int(c) for c in str(n)]
    k = len(digits)
    return sum(d**k for d in digits) == n

def is_palindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return x == rev or x == rev // 10

if __name__ == "__main__":
    print("153 is Armstrong?", is_armstrong(153))
    print("1221 is Palindrome?", is_palindrome(1221))
''')

with open(os.path.join(p6_code, "Solution.java"), "w", encoding="utf-8") as f:
    f.write('''public class Solution {
    public static boolean isArmstrong(long n) {
        if (n < 0) return false;
        long temp = n;
        int k = 0;
        while (temp > 0) {
            k++;
            temp /= 10;
        }
        long sum = 0;
        temp = n;
        while (temp > 0) {
            long d = temp % 10;
            sum += Math.pow(d, k);
            temp /= 10;
        }
        return sum == n;
    }

    public static boolean isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) return false;
        int rev = 0;
        while (x > rev) {
            rev = rev * 10 + x % 10;
            x /= 10;
        }
        return x == rev || x == rev / 10;
    }

    public static void main(String[] args) {
        System.out.println("153 is Armstrong? " + isArmstrong(153));
        System.out.println("1221 is Palindrome? " + isPalindrome(1221));
    }
}
''')

with open(os.path.join(prob_dir, "006-armstrong-and-palindrome-number.md"), "w", encoding="utf-8") as f:
    f.write('''# Armstrong Number & Half-Reversal Integer Palindrome Check

[← Back to Module Overview](../README.md) · [Concepts: Digit Manipulation & Armstrong](../concepts/03-armstrong-and-digit-math.md)

---

## 1. Problem Overview
- **Name:** Armstrong Number and Palindrome Number
- **Difficulty:** Easy
- **Tier:** A (Flagship Foundation)
- **Pattern:** `#math`, `#digit-manipulation`
- **External Links:** [LeetCode 9: Palindrome Number](https://leetcode.com/problems/palindrome-number/) · [GeeksforGeeks: Armstrong Numbers](https://www.geeksforgeeks.org/program-for-armstrong-numbers/)

---

## 2. Complexity Analysis
- **Time Complexity:** $\mathcal{O}(\log_{10} N)$
- **Space Complexity:** $\mathcal{O}(1)$
''')

print("All 6 Tier A problems and solutions created successfully.")
