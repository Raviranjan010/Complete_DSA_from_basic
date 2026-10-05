# Greatest Common Divisor (GCD) & Euclidean Algorithm

## 1. Motivation
Finding the greatest common divisor of two integers is essential in simplifying fractions, modular arithmetic, and geometric algorithms.

## 2. Intuition
Euclid discovered that the GCD of two numbers also divides their difference:
$$\gcd(a, b) = \gcd(b, a \pmod b)$$
Base case: $\gcd(a, 0) = a$.

## 3. Complexity
- Time Complexity: $O(\log(\min(a, b)))$ (Lame's Theorem)
- Space Complexity: $O(\log(\min(a, b)))$ recursive call stack
