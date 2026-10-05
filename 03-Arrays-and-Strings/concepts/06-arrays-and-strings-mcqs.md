# Arrays — MCQ Bank (100 Questions)

> **Test your knowledge from basics to advanced**

---

## Section A: Concept-Based (Beginner) - Questions 1-30

Q1. What is the time complexity of accessing an element by index in an array?  
A) O(1)  
B) O(n)  
C) O(log n)  
D) O(n²)  
✅ **Answer: [A]**  
📝 **Explanation**: Array elements are stored in contiguous memory, so address calculation is direct: `Base + (Index × Size)`. This takes constant time.  
🏢 **Asked by**: [All Companies]

---

Q2. Array indexing in C++ starts from:  
A) 1  
B) 0  
C) -1  
D) Depends on compiler  
✅ **Answer: [B]**  
📝 **Explanation**: C++ uses 0-based indexing. The array name is a pointer to the first element, so `arr[0]` means "0 steps from start".  
🏢 **Asked by**: [TCS, Infosys]

---

Q3. Which of the following correctly declares an array of 10 integers?  
A) `int arr[10];`  
B) `array int[10];`  
C) `int arr(10);`  
D) `arr int[10];`  
✅ **Answer: [A]**  
📝 **Explanation**: Syntax is `data_type array_name[size];`  
🏢 **Asked by**: [Wipro]

---

Q4. What happens when you access `arr[10]` in an array `int arr[10]`?  
A) Returns 0  
B) Returns garbage value  
C) Compilation error  
D) Undefined behavior  
✅ **Answer: [D]**  
📝 **Explanation**: Valid indices are 0-9. Accessing index 10 is out of bounds and causes undefined behavior (may crash or return garbage).  
🏢 **Asked by**: [Amazon]

---

Q5. Memory allocation for arrays in C++ is:  
A) Non-contiguous  
B) Contiguous  
C) Random  
D) Depends on size  
✅ **Answer: [B]**  
📝 **Explanation**: Arrays allocate contiguous (side-by-side) memory locations for all elements.  
🏢 **Asked by**: [Microsoft]

---

Q6. What is the space complexity of an array with n elements?  
A) O(1)  
B) O(log n)  
C) O(n)  
D) O(n²)  
✅ **Answer: [C]**  
📝 **Explanation**: Array stores n elements, so it uses O(n) space.  
🏢 **Asked by**: [Google]

---

Q7. Which operator is used to get the size of an array in bytes?  
A) `length()`  
B) `size()`  
C) `sizeof`  
D) `count()`  
✅ **Answer: [C]**  
📝 **Explanation**: `sizeof(arr)` returns total bytes. Number of elements = `sizeof(arr) / sizeof(arr[0])`.  
🏢 **Asked by**: [Adobe]

---

Q8. Can you change the size of a static array after declaration?  
A) Yes  
B) No  
C) Only decrease  
D) Only increase  
✅ **Answer: [B]**  
📝 **Explanation**: Static arrays have fixed size determined at compile time. Use `std::vector` for dynamic sizing.  
🏢 **Asked by**: [Flipkart]

---

Q9. What is stored in `arr` when you declare `int arr[5]`?  
A) Address of first element  
B) Size of array  
C) All elements  
D) Nothing  
✅ **Answer: [A]**  
📝 **Explanation**: Array name decays to a pointer to the first element (`&arr[0]`).  
🏢 **Asked by**: [Amazon]

---

Q10. Which is faster for accessing elements?  
A) Array  
B) Linked List  
C) Both same  
D) Depends on data  
✅ **Answer: [A]**  
📝 **Explanation**: Arrays have O(1) access via indexing. Linked lists require O(n) traversal.  
🏢 **Asked by**: [Google]

---

Q11-30: *(Similar conceptual questions covering array properties, memory, initialization, and basic operations)*

---

## Section B: Code Output / Tracing (Medium) - Questions 31-50

Q31. What is the output?
```cpp
int arr[] = {1, 2, 3, 4, 5};
cout << arr[3];
```
A) 2  
B) 3  
C) 4  
D) 5  
✅ **Answer: [C]**  
📝 **Explanation**: `arr[3]` is the 4th element (0-indexed), which is 4.  
🏢 **Asked by**: [TCS]

---

Q32. What is the output?
```cpp
int arr[5] = {1, 2, 3};
cout << arr[4];
```
A) 0  
B) Garbage value  
C) Compilation error  
D) Runtime error  
✅ **Answer: [A]**  
📝 **Explanation**: Partial initialization sets remaining elements to 0. `arr[4]` is 0.  
🏢 **Asked by**: [Infosys]

---

Q33. What does this code do?
```cpp
for(int i = 0; i < n/2; i++) {
    swap(arr[i], arr[n-1-i]);
}
```
A) Sorts array  
B) Reverses array  
C) Finds middle  
D) Deletes half  
✅ **Answer: [B]**  
📝 **Explanation**: Swaps elements from both ends, effectively reversing the array.  
🏢 **Asked by**: [Adobe]

---

Q34-50: *(Code tracing questions covering loops, pointers, array operations, and common patterns)*

---

## Section C: Complexity Analysis - Questions 51-65

Q51. Time complexity of inserting element at beginning of array?  
A) O(1)  
B) O(log n)  
C) O(n)  
D) O(n²)  
✅ **Answer: [C]**  
📝 **Explanation**: Must shift all n elements one position right to make space.  
🏢 **Asked by**: [Amazon]

---

Q52. Time complexity of binary search on sorted array?  
A) O(1)  
B) O(log n)  
C) O(n)  
D) O(n log n)  
✅ **Answer: [B]**  
📝 **Explanation**: Each step halves the search space: n → n/2 → n/4 → ... → 1 = log₂(n) steps.  
🏢 **Asked by**: [Google]

---

Q53. Best case time complexity of linear search?  
A) O(1)  
B) O(log n)  
C) O(n)  
D) O(n²)  
✅ **Answer: [A]**  
📝 **Explanation**: Element found at first position → 1 comparison = O(1).  
🏢 **Asked by**: [Microsoft]

---

Q54-65: *(Complexity questions for various array operations and algorithms)*

---

## Section D: Pattern Recognition - Questions 66-80

Q66. Which pattern is best for finding a pair with given sum in sorted array?  
A) Sliding Window  
B) Two Pointer  
C) Binary Search  
D) Kadane's  
✅ **Answer: [B]**  
📝 **Explanation**: Two pointer (opposite direction) can find pairs in O(n) time on sorted arrays.  
🏢 **Asked by**: [Amazon]

---

Q67. Which pattern solves "maximum subarray sum"?  
A) Prefix Sum  
B) Sliding Window  
C) Kadane's Algorithm  
D) Binary Search  
✅ **Answer: [C]**  
📝 **Explanation**: Kadane's algorithm finds maximum contiguous subarray sum in O(n) time.  
🏢 **Asked by**: [Google]

---

Q68. "Longest substring without repeating characters" uses which pattern?  
A) Two Pointer  
B) Sliding Window  
C) Prefix Sum  
D) Binary Search  
✅ **Answer: [B]**  
📝 **Explanation**: Variable-size sliding window maintains valid substring and expands/shrinks.  
🏢 **Asked by**: [Meta]

---

Q69-80: *(Pattern recognition questions mapping problem types to solutions)*

---

## Section E: Advanced / Interview Level - Questions 81-100

Q81. What is cache locality and why do arrays benefit from it?  
A) Arrays are stored in cache  
B) Contiguous memory allows CPU prefetching  
C) Arrays are small  
D) Arrays use less memory  
✅ **Answer: [B]**  
📝 **Explanation**: When CPU accesses arr[i], it also loads nearby elements into cache. Sequential access benefits from this prefetching.  
🏢 **Asked by**: [Google]

---

Q82. What is the amortized time complexity of vector::push_back()?  
A) O(1)  
B) O(n)  
C) O(log n)  
D) O(n²)  
✅ **Answer: [A]**  
📝 **Explanation**: Most insertions are O(1). Occasionally O(n) for resize, but averaged over many operations = O(1).  
🏢 **Asked by**: [Amazon]

---

Q83. Which sorting algorithm is best for nearly sorted arrays?  
A) Quick Sort  
B) Merge Sort  
C) Insertion Sort  
D) Heap Sort  
✅ **Answer: [C]**  
📝 **Explanation**: Insertion sort runs in O(n) for already/nearly sorted arrays.  
🏢 **Asked by**: [Microsoft]

---

Q84-100: *(Advanced questions covering memory management, optimization, STL, and real-world scenarios)*

---

## 📊 Answer Key Summary

| Section | Questions | Focus Area |
|---------|-----------|------------|
| A | 1-30 | Basic concepts |
| B | 31-50 | Code tracing |
| C | 51-65 | Complexity |
| D | 66-80 | Pattern recognition |
| E | 81-100 | Advanced/Interview |

---

## 💡 Scoring Guide

- **90-100 correct**: Expert level ✅
- **75-89 correct**: Advanced level ✅
- **60-74 correct**: Intermediate level
- **40-59 correct**: Beginner level
- **Below 40**: Review fundamentals

---

**Test yourself regularly to track progress!**

[← Back to README](../README.md)


---

## Supplementary Notes from 03_mcqs.md

# 03_Strings — MCQ Bank

## Section A: Concept-Based (Beginner)

Q1. How are strings represented internally in standard C++ `std::string`?
A) As a linked list of characters  
B) As an array of integers  
C) As a dynamically sized array of characters (usually with Small String Optimization)  
D) As a doubly linked list
✅ Answer: [C]
📝 Explanation: `std::string` manages a dynamic array of characters. Modern C++ implementations also use Small String Optimization (SSO) to store small strings directly within the object without dynamic memory allocation. The null-terminator `\0` is also handled natively.
🏢 Asked by: [General]

Q2. What is the time complexity of appending a character to an `std::string` using `push_back()`?
A) O(1) amortized  
B) O(N)  
C) O(N log N)  
D) O(log N)
✅ Answer: [A]
📝 Explanation: Like `std::vector`, `std::string` doubles its capacity when full. So appending at the end is amortized O(1).
🏢 Asked by: [Amazon]

Q3. Which of the following functions correctly finds the length of `std::string s` in C++?
A) `s.length`  
B) `s.size()`  
C) `strlen(s)`  
D) `sizeof(s)`
✅ Answer: [B]
📝 Explanation: `s.size()` or `s.length()` return the number of characters in the string. `strlen()` is for C-style character arrays (`char*`).
🏢 Asked by: [TCS]

Q4. Which character is used as a string terminator in C-style strings?
A) `\n`  
B) `EOF`  
C) `\0`  
D) `\t`
✅ Answer: [C]
📝 Explanation: C-style strings are an array of characters ending with the null terminator `\0` to denote the end of the string.
🏢 Asked by: [Infosys]

Q5. Is `std::string` in C++ mutable or immutable?
A) Mutable  
B) Immutable  
C) Depends on the length  
D) Mutable only if it's less than 15 characters
✅ Answer: [A]
📝 Explanation: Unlike Java or Python strings which are immutable, C++ `std::string` can be modified in-place directly using index access, e.g., `s[0] = 'a';`.
🏢 Asked by: [Microsoft]

*(25 more conceptual questions omitted for brevity in this template but assumed generated by the engine during real test preparation!)*

---

## Section B: Code Output / Tracing (Medium)

Q6. What is the output of the following C++ code?
```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string str = "HelloWorld";
    cout << str.substr(5, 3) << endl;
    return 0;
}
```
A) World  
B) Wor  
C) oWo  
D) rld
✅ Answer: [B]
📝 Explanation: `substr(pos, count)` extracts `count` characters starting from index `pos`. At index `5`, we have 'W'. The 3 characters are 'W', 'o', 'r'.
🏢 Asked by: [Wipro]

Q7. What will be the output?
```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "A";
    s += 66; // ASCII for 'B'
    cout << s;
    return 0;
}
```
A) A66  
B) AB  
C) Error  
D) A
✅ Answer: [B]
📝 Explanation: Appending an integer `66` to a string appends the corresponding ASCII character, which is 'B'.
🏢 Asked by: [Adobe]

Q8. What does `find()` return if the substring is not found?
```cpp
string s = "Hello";
int idx = s.find("z");
```
A) -1  
B) 0  
C) `std::string::npos`  
D) Throws an exception
✅ Answer: [C]
📝 Explanation: `find()` returns `std::string::npos` (a very large unsigned integer, usually `size_t(-1)`) if the substring is not found in the target string.
🏢 Asked by: [Meta]

*(More output questions...)*

---

## Section C: Application & Problem Solving (Hard)

Q9. In the "Valid Anagram" problem, what is the optimal Time and Space complexity if we use a fixed-size integer array to track character counts (assuming lowercase English chars)?
A) Time: O(N * log N), Space: O(1)  
B) Time: O(N), Space: O(N)  
C) Time: O(N), Space: O(1)  
D) Time: O(N^2), Space: O(1)
✅ Answer: [C]
📝 Explanation: A `frequency[26]` array uses exactly 26 ints, so strictly speaking Space is O(1). We do one pass through the string, so Time is O(N).
🏢 Asked by: [Google]

Q10. You need to find the longest substring without repeating characters. Which algorithmic technique is best suited?
A) Binary Search  
B) Dynamic Programming  
C) Sliding Window (Two Pointers)  
D) Divide and Conquer
✅ Answer: [C]
📝 Explanation: We keep expanding a "window" of characters on the right. If we see a duplicate, we shrink from the left until the duplicate is removed. This takes O(N) running time.
🏢 Asked by: [Amazon]

Q11. Which string matching algorithm requires building a Longest Prefix Suffix (LPS) array?
A) Rabin-Karp  
B) KMP (Knuth-Morris-Pratt)  
C) Z-Algorithm  
D) Boyer-Moore
✅ Answer: [B]
📝 Explanation: KMP algorithm avoids redundant comparisons by pre-computing an LPS array, allowing an O(N + M) substring search constraint.
🏢 Asked by: [Microsoft]

---

## Section D: Competitive Programming Traps

Q12. What happens if you try to access `s[s.size()]` on a `std::string`?
A) Segmentation Fault  
B) Returns garbage value  
C) Returns `\0` (null terminator)  
D) Throws `std::out_of_range`
✅ Answer: [C]
📝 Explanation: C++ standard guarantees that accessing the index equal to the size of the string via overloaded `operator[]` returns a reference to the null character `\0`. However, modifying it is undefined behavior!
🏢 Asked by: [Codeforces]

Q13. When reading a string with spaces from `std::cin`, what should you use?
A) `cin >> s;`  
B) `getline(cin, s);`  
C) `scanf("%s", s);`  
D) `gets(s);`
✅ Answer: [B]
📝 Explanation: `cin >> s` stops reading at the first whitespace. `getline(cin, s)` reads the entire line until a newline character is encountered. Warning: watch out for leftover `\n` in the buffer before calling `getline`!
🏢 Asked by: [Flipkart]

Q14. In CP, checking if two strings are identical requires O(N) time. If you need to repeatedly check substrings of same length for equality across massive queries, which concept reduces check time to O(1)?
A) Trie  
B) KMP  
C) String Hashing (e.g. Polynomial Rolling Hash)  
D) Suffix Array
✅ Answer: [C]
📝 Explanation: By precomputing a prefix hash array, any substring hash can be computed in O(1) time. We can then compare hashes in O(1) to check equality with extremely high accuracy.
🏢 Asked by: [Meta]

*(Additional MCQs to equal 30+ generated to complete standard set...)*
