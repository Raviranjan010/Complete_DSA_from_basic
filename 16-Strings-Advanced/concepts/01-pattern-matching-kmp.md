# String Pattern Matching Algorithms: Naive & KMP

## 1. Problem Formulation
Given text $T$ of length $n$ and pattern $P$ of length $m$, find all occurrences of $P$ in $T$.

## 2. Naive Algorithm
$O((n - m + 1) \times m)$ worst case.

## 3. Knuth-Morris-Pratt (KMP)
Constructs $\pi$ table (longest proper prefix which is also suffix) in $O(m)$ time, achieving overall $O(n + m)$ search time.
