# 09 — Hashing — Complete Notes

> **What You'll Learn**: Hash tables, unordered_map, collision handling, frequency maps, two-sum pattern  
> **Prerequisites**: Arrays, STL basics (Topics 02, 00)  
> **Time Required**: 1 week (10-12 hours)  
> **Importance**: 🌟🌟🌟🌟🌟 (Extremely high - most used in interviews)

---

## 1. What is Hashing? (Real-World Analogy)

Imagine a **library with a digital catalog system**:

**Without Hashing**: Search every shelf one by one to find a book (O(n)) 😫

**With Hashing**: Use the catalog number to go directly to the book's location (O(1)) ✨

**How it works**:
```
Book: "Harry Potter"
Hash Function → Shelf 7, Position 3
Go directly there! No searching needed!
```

**Hash Table** = Data structure that maps keys to values using a hash function

💡 **TRICK**: **Hashing Mnemonic**: "Magic index calculator" - gives you exact location instantly!

---

## 2. Core Concepts

### Hash Function
Takes a key and returns an index:
```cpp
hash("apple") = 5
hash("banana") = 12
hash("orange") = 3
```

### Collision
When two keys map to the same index:
```cpp
hash("apple") = 5
hash("grape") = 5  // Collision!
```

### Collision Resolution
1. **Chaining**: Store multiple items at same index (linked list)
2. **Open Addressing**: Find next empty slot

---

## 3. Visual Diagram: Hash Table

```
┌─────────────────────────────────────────────────────────────┐
│              HASH TABLE (Chaining)                           │
├──────┬──────────────────────────────────────────────────────┤
│Index │  Chain (Linked List)                                  │
├──────┼──────────────────────────────────────────────────────┤
│  0   │  NULL                                                 │
│  1   │  NULL                                                 │
│  2   │  ["key2" → 200] → NULL                                │
│  3   │  ["orange" → 3] → NULL                                │
│  4   │  NULL                                                 │
│  5   │  ["apple" → 1] → ["grape" → 4] → NULL                │
│  6   │  NULL                                                 │
│  ... │  ...                                                  │
│  12  │  ["banana" → 2] → NULL                                │
└──────┴──────────────────────────────────────────────────────┘

Operations:
- Insert: O(1) average
- Search: O(1) average
- Delete: O(1) average
```

---

## 4. C++ Implementation

### Using unordered_map (STL Hash Table)

```cpp
#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int main() {
    // Create hash table
    unordered_map<string, int> phoneBook;
    
    // INSERT - O(1)
    phoneBook["Alice"] = 12345;
    phoneBook["Bob"] = 67890;
    phoneBook["Charlie"] = 11111;
    
    // SEARCH - O(1)
    if(phoneBook.count("Alice")) {
        cout << "Alice's number: " << phoneBook["Alice"] << endl;  // 12345
    }
    
    // UPDATE - O(1)
    phoneBook["Alice"] = 99999;
    
    // DELETE - O(1)
    phoneBook.erase("Bob");
    
    // ITERATE - O(n)
    for(auto& pair : phoneBook) {
        cout << pair.first << ": " << pair.second << endl;
    }
    
    return 0;
}
```

---

## 5. Essential Hashing Patterns

### Pattern 1: Two Sum (MOST ASKED!)

```cpp
// Time: O(n), Space: O(n)
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> numMap;  // value → index
    
    for(int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        
        // Check if complement exists
        if(numMap.count(complement)) {
            return {numMap[complement], i};
        }
        
        // Store current number
        numMap[nums[i]] = i;
    }
    
    return {};  // No solution
}

int main() {
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    
    vector<int> result = twoSum(nums, target);
    cout << "Indices: " << result[0] << ", " << result[1] << endl;
    // Output: 0, 1 (nums[0]=2, nums[1]=7, 2+7=9)
    
    return 0;
}
```

**Dry Run** (`nums=[2,7,11,15]`, target=9):
```
i=0, nums[0]=2:
  complement = 9-2 = 7
  7 not in map
  Add: {2: 0}

i=1, nums[1]=7:
  complement = 9-7 = 2
  2 IS in map! → Found!
  Return {0, 1} ✓
```

💡 **TRICK**: **Two Sum Trick**: Instead of checking all pairs, store seen numbers and check if complement exists!

---

### Pattern 2: Frequency Map

```cpp
// Count frequency of elements
unordered_map<int, int> frequency(const vector<int>& nums) {
    unordered_map<int, int> freq;
    
    for(int num : nums) {
        freq[num]++;  // Increment count
    }
    
    return freq;
}

int main() {
    vector<int> nums = {1, 2, 2, 3, 3, 3, 4};
    auto freq = frequency(nums);
    
    for(auto& pair : freq) {
        cout << pair.first << " appears " << pair.second << " times" << endl;
    }
    // Output:
    // 1 appears 1 times
    // 2 appears 2 times
    // 3 appears 3 times
    // 4 appears 1 times
    
    return 0;
}
```

---

### Pattern 3: Group Anagrams

```cpp
// Time: O(n × k log k), Space: O(n × k)
// n = number of strings, k = max length
vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> groups;
    
    for(string& s : strs) {
        string sorted = s;
        sort(sorted.begin(), sorted.end());  // Sort to get key
        groups[sorted].push_back(s);  // Group anagrams
    }
    
    vector<vector<string>> result;
    for(auto& pair : groups) {
        result.push_back(pair.second);
    }
    
    return result;
}

int main() {
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    auto groups = groupAnagrams(strs);
    
    // Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
    for(auto& group : groups) {
        cout << "[";
        for(string& word : group) {
            cout << word << " ";
        }
        cout << "]" << endl;
    }
    
    return 0;
}
```

---

## 6. All Operations with Time & Space Complexity

| Operation | Average | Worst Case |
|-----------|---------|------------|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Space | O(n) | O(n) |

**Note**: Worst case O(n) when all keys hash to same index (rare with good hash function)

---

## 7. Common Patterns & Tricks

### 💡 TRICK 1: Custom Hash for Pairs
```cpp
struct pair_hash {
    size_t operator()(const pair<int, int>& p) const {
        return p.first ^ p.second;
    }
};

unordered_map<pair<int, int>, int, pair_hash> myMap;
```

### 💡 TRICK 2: Count Distinct Elements
```cpp
unordered_set<int> distinct(nums.begin(), nums.end());
int count = distinct.size();
```

### 💡 TRICK 3: Check Duplicates
```cpp
bool hasDuplicate(const vector<int>& nums) {
    unordered_set<int> seen;
    for(int num : nums) {
        if(seen.count(num)) return true;
        seen.insert(num);
    }
    return false;
}
```

---

## 8. Interview Questions

### Most Asked:
1. **Two Sum** 🏢 [Google] 📅 [Very High]
2. **Group Anagrams** 🏢 [Amazon] 📅 [Very High]
3. **Longest Consecutive Sequence** 🏢 [Google]
4. **Top K Frequent Elements** 🏢 [Meta]
5. **Valid Sudoku** 🏢 [Microsoft]

---

## 9. Practice Problems

### 🟢 Easy:
1. Two Sum
2. Contains Duplicate
3. Valid Anagram

### 🟡 Medium:
4. Group Anagrams 🏢 [Amazon]
5. Longest Consecutive Sequence
6. Top K Frequent Elements

### 🔴 Hard:
7. Longest Substring Without Repeating Characters
8. Minimum Window Substring

---

## 10. Glossary

| Term | Definition |
|------|------------|
| **Hash Table** | Data structure mapping keys to values |
| **Hash Function** | Function converting key to index |
| **Collision** | Two keys mapping to same index |
| **Chaining** | Collision resolution using linked lists |
| **Load Factor** | Ratio of filled slots to total slots |
| **unordered_map** | C++ STL hash table implementation |

---

**🎉 You've mastered Hashing!**

**Next**: [10_Trees](../10_Trees/10_notes.md)

[← Back to README](../README.md)


---

## Supplementary Notes from 07-Hashing.md

# 🗃️ 07 — Hashing (HashSet & HashMap)

> **Explain Like I'm 5:** Imagine a coat-check counter. You hand over your coat, get a ticket, and later that ticket instantly locates your exact coat — without the clerk scanning through every single coat in the building. 
> A **hash** is that instant-lookup ticket. Instead of scanning a whole array ($O(n)$ time), you ask "is it there?" and get an answer *instantly* ($O(1)$ time).

---

## ⚙️ Under the Hood: How Hashing Works

A HashTable (the engine behind HashMap and HashSet) maps keys to values using a combination of a **Hash Function** and a **Bucket Array**.

### 1. The Hash Function
A mathematical function that converts any key (like a string `"apple"` or integer `482`) into an integer index within the range of our bucket array:

$$\text{Bucket Index} = \text{Hash}(Key) \pmod{\text{Bucket Size}}$$

A good hash function distributes keys uniformly across the array to avoid clusters.

### 2. Collisions & Collision Resolution
Since there are infinite possible keys but a finite number of buckets, two different keys will eventually hash to the exact same index. This is a **Collision**.
There are two primary ways to resolve collisions:

#### Method A: Separate Chaining (Used by Java's HashMap)
Each slot in the bucket array points to a linked list (or a balanced tree) of elements that hashed to that same index.

```
Bucket Array:
┌───┐
│ 0 │ ──► [ Key: "apple", Val: 10 ] ──► NULL
├───┤
│ 1 │ ──► NULL
├───┤
│ 2 │ ──► [ Key: "banana", Val: 3 ] ──► [ Key: "cherry", Val: 7 ] ──► NULL
├───┤
│ 3 │ ──► NULL
└───┘
```

#### Method B: Open Addressing (Linear Probing)
If a slot is full, the computer searches sequentially for the next available empty slot in the array.

### 3. Load Factor & Rehashing
The **Load Factor ($\alpha$)** measures how full the HashTable is:

$$\alpha = \frac{\text{Number of Stored Keys}}{\text{Total Bucket Size}}$$

- When $\alpha$ exceeds a threshold (typically **`0.75`**), lookup performance begins to degrade because collision chains grow longer.
- The table triggers **Rehashing**: it doubles the bucket array size, creates a new hash function modulo, and moves all elements to their new locations. This is an $O(n)$ operation but happens infrequently, maintaining an **amortized $O(1)$** insertion time.

---

## 📊 HashSet vs. HashMap

| Structure | Purpose | Internal Mechanism | Typical Question |
| :--- | :--- | :--- | :--- |
| **HashSet** | Stores unique keys. | A HashMap under the hood with a dummy value. | *"Have I seen this element before?"* |
| **HashMap** | Maps unique keys to values. | A table of Key-Value pairs. | *"What information is associated with this key?"* |

---

## 🎯 Practice Problems & Worked Solutions

Work through these problems in order to see how Hashing transforms nested loops into linear lookups.

| # | Problem | Difficulty | Link | Key Idea |
|---|---|---|---|---|
| 1 | Contains Duplicate | Easy | [LeetCode](https://leetcode.com/problems/contains-duplicate/) | HashSet uniqueness check. |
| 2 | Two Sum | Easy | [LeetCode](https://leetcode.com/problems/two-sum/) | Map target complements to indices. |
| 3 | Isomorphic Strings | Easy | [LeetCode](https://leetcode.com/problems/isomorphic-strings/) | Two-way mapping check. |
| 4 | Find Common Characters | Easy | [LeetCode](https://leetcode.com/problems/find-common-characters/) | Intersecting frequency counts. |
| 5 | Sort Characters By Frequency | Medium | [LeetCode](https://leetcode.com/problems/sort-characters-by-frequency/) | Count frequencies, sort keys by value. |
| 6 | Find The Difference | Easy | [LeetCode](https://leetcode.com/problems/find-the-difference/) | Balance counts or cancel out using XOR. |

---

### Solution 1: Contains Duplicate

**Intuition:** 
As we traverse the array, check if the current element is already in our `seen` set.
- If it is, we found a duplicate -> return `true`.
- Otherwise, add the element to the set and continue.

**Complexity:**
- **Time:** $O(n)$ — Single pass traversal.
- **Space:** $O(n)$ — In the worst case, we store all $n$ unique elements in the set.

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public boolean containsDuplicate(int[] nums) {
    HashSet<Integer> seen = new HashSet<>();
    for (int num : nums) {
        if (seen.contains(num)) {
            return true; // Found duplicate
        }
        seen.add(num);
    }
    return false;
}
```

#### Python
```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True # Found duplicate
        seen.add(num)
    return False
```

#### C++
```cpp
bool containsDuplicate(vector<int>& nums) {
    unordered_set<int> seen;
    for (int num : nums) {
        if (seen.count(num)) {
            return true; // Found duplicate
        }
        seen.insert(num);
    }
    return false;
}
```
</details>

---

### Solution 2: Two Sum

**Intuition:**
For each number `nums[i]`, we need to find if its complement `target - nums[i]` exists in the array.
Instead of checking every pair ($O(n^2)$), we store each visited number and its index in a HashMap. At each step, we look up if `target - nums[i]` is in the map. If it is, we return their indices.

**Complexity:**
- **Time:** $O(n)$ — One-pass traversal.
- **Space:** $O(n)$ — Store elements in the HashMap.

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int[] twoSum(int[] nums, int target) {
    HashMap<Integer, Integer> map = new HashMap<>(); // Value -> Index
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement)) {
            return new int[]{map.get(complement), i};
        }
        map.put(nums[i], i);
    }
    return new int[]{};
}
```

#### Python
```python
def two_sum(nums, target):
    mp = {} # Value -> Index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in mp:
            return [mp[complement], i]
        mp[num] = i
    return []
```

#### C++
```cpp
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> mp; // Value -> Index
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (mp.count(complement)) {
            return {mp[complement], i};
        }
        mp[nums[i]] = i;
    }
    return {};
}
```
</details>

---

### Solution 3: Isomorphic Strings

**Intuition:**
A mapping must exist both ways. For example, if `s = "egg"` and `t = "add"`, then `'e'` maps to `'a'` and `'g'` maps to `'d'`. Additionally, `'a'` must map back to `'e'` and `'d'` back to `'g'`. We use two HashMaps to track these mappings.

**Complexity:**
- **Time:** $O(n)$
- **Space:** $O(1)$ (The character set is bounded by ASCII size, at most 256 keys).

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public boolean isIsomorphic(String s, String t) {
    HashMap<Character, Character> sToT = new HashMap<>();
    HashMap<Character, Character> tToS = new HashMap<>();
    
    for (int i = 0; i < s.length(); i++) {
        char a = s.charAt(i);
        char b = t.charAt(i);
        
        if (sToT.containsKey(a) && sToT.get(a) != b) return false;
        if (tToS.containsKey(b) && tToS.get(b) != a) return false;
        
        sToT.put(a, b);
        tToS.put(b, a);
    }
    return true;
}
```

#### Python
```python
def is_isomorphic(s, t):
    s_to_t, t_to_s = {}, {}
    for a, b in zip(s, t):
        if a in s_to_t and s_to_t[a] != b:
            return False
        if b in t_to_s and t_to_s[b] != a:
            return False
        s_to_t[a] = b
        t_to_s[b] = a
    return True
```

#### C++
```cpp
bool isIsomorphic(string s, string t) {
    unordered_map<char, char> sToT, tToS;
    for (int i = 0; i < s.size(); i++) {
        char a = s[i], b = t[i];
        if (sToT.count(a) && sToT[a] != b) return false;
        if (tToS.count(b) && tToS[b] != a) return false;
        sToT[a] = b;
        tToS[b] = a;
    }
    return true;
}
```
</details>

---

### Solution 4: Find Common Characters

**Intuition:**
For each string, calculate the frequency count of each character. Keep a global minimum frequency list `minFreq` of size 26. For each letter, update `minFreq[c] = min(minFreq[c], currentWordFreq[c])`.

**Complexity:**
- **Time:** $O(n \times L)$ where $n$ is the number of words, and $L$ is the average word length.
- **Space:** $O(1)$ auxiliary space (frequency arrays are fixed at size 26).

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public List<String> commonChars(String[] words) {
    int[] minFreq = new int[26];
    Arrays.fill(minFreq, Integer.MAX_VALUE);
    
    for (String w : words) {
        int[] freq = new int[26];
        for (char c : w.toCharArray()) {
            freq[c - 'a']++;
        }
        for (int i = 0; i < 26; i++) {
            minFreq[i] = Math.min(minFreq[i], freq[i]);
        }
    }
    
    List<String> result = new ArrayList<>();
    for (int i = 0; i < 26; i++) {
        while (minFreq[i] > 0) {
            result.add(String.valueOf((char) ('a' + i)));
            minFreq[i]--;
        }
    }
    return result;
}
```

#### Python
```python
from collections import Counter

def common_chars(words):
    # Intersect frequencies using Counter & intersection
    common = Counter(words[0])
    for w in words[1:]:
        common &= Counter(w)
    return list(common.elements())
```

#### C++
```cpp
vector<string> commonChars(vector<string>& words) {
    vector<int> minFreq(26, INT_MAX);
    for (string& w : words) {
        vector<int> freq(26, 0);
        for (char c : w) {
            freq[c - 'a']++;
        }
        for (int i = 0; i < 26; i++) {
            minFreq[i] = min(minFreq[i], freq[i]);
        }
    }
    vector<string> result;
    for (int i = 0; i < 26; i++) {
        while (minFreq[i] > 0) {
            result.push_back(string(1, 'a' + i));
            minFreq[i]--;
        }
    }
    return result;
}
```
</details>

---

### Solution 5: Sort Characters By Frequency

**Intuition:**
Use a HashMap to build character frequency counts. Then, sort the character keys based on their values (frequencies) in descending order. Construct the result string by appending each character repeated by its count.

**Complexity:**
- **Time:** $O(n + k \log k)$ where $n$ is string length, and $k$ is unique characters count ($k \le 256$, so essentially $O(n)$).
- **Space:** $O(n)$ (for storing frequencies and building the string).

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public String frequencySort(String s) {
    HashMap<Character, Integer> counts = new HashMap<>();
    for (char c : s.toCharArray()) {
        counts.put(c, counts.getOrDefault(c, 0) + 1);
    }
    
    // Sort keys based on count value
    List<Character> chars = new ArrayList<>(counts.keySet());
    chars.sort((a, b) -> counts.get(b) - counts.get(a));
    
    StringBuilder sb = new StringBuilder();
    for (char c : chars) {
        int count = counts.get(c);
        for (int i = 0; i < count; i++) {
            sb.append(c);
        }
    }
    return sb.toString();
}
```

#### Python
```python
from collections import Counter

def frequency_sort(s):
    freq = Counter(s)
    # most_common() returns list of (element, count) sorted by count descending
    return "".join(c * count for c, count in freq.most_common())
```

#### C++
```cpp
string frequencySort(string s) {
    unordered_map<char, int> freq;
    for (char c : s) freq[c]++;
    
    vector<pair<int, char>> arr;
    for (auto p : freq) {
        arr.push_back({p.second, p.first});
    }
    // Sort in descending order
    sort(arr.rbegin(), arr.rend());
    
    string result = "";
    for (auto p : arr) {
        result += string(p.first, p.second);
    }
    return result;
}
```
</details>

---

### Solution 6: Find The Difference

**Intuition:**
1. **Counting method:** Count frequencies in `t`, subtract using characters in `s`. The character left with count $> 0$ is the extra character.
2. **XOR method:** Since $X \oplus X = 0$, XORing all characters from both strings will cancel out duplicate characters, leaving only the extra one.

**Complexity:**
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java (XOR Version)
```java
public char findTheDifference(String s, String t) {
    char extra = 0;
    for (int i = 0; i < s.length(); i++) {
        extra ^= s.charAt(i);
    }
    for (int i = 0; i < t.length(); i++) {
        extra ^= t.charAt(i);
    }
    return extra;
}
```

#### Python (XOR Version)
```python
def find_the_difference(s, t):
    extra = 0
    for ch in s:
        extra ^= ord(ch)
    for ch in t:
        extra ^= ord(ch)
    return chr(extra)
```

#### C++ (XOR Version)
```cpp
char findTheDifference(string s, string t) {
    char extra = 0;
    for (char c : s) extra ^= c;
    for (char c : t) extra ^= c;
    return extra;
}
```
</details>

<details>
<summary>📋 Step-by-Step Dry Run</summary>

Input: `s = "abcd"`, `t = "abcde"`

Using XOR property ($X \oplus X = 0, X \oplus 0 = X$):
- `extra = 0`
- XOR `s`: `'a' ^ 'b' ^ 'c' ^ 'd'`
- XOR `t`: `'a' ^ 'b' ^ 'c' ^ 'd' ^ 'e'`
- Combined XOR: `('a' ^ 'a') ^ ('b' ^ 'b') ^ ('c' ^ 'c') ^ ('d' ^ 'd') ^ 'e'`
- Pairs cancel out to 0: `0 ^ 0 ^ 0 ^ 0 ^ 'e' = 'e'`

**Result:** `'e'` ✅
</details>

---

## 🎓 Viva Questions & Answers

### Q1: What is a Hash Table, Hash Function, and Load Factor?
**Answer:**
- **Hash Table:** A data structure that stores key-value pairs using array indexing under the hood.
- **Hash Function:** A function that maps an arbitrary key (e.g. string, object) to a fixed-size integer array index.
- **Load Factor:** The ratio of total items stored $n$ to total table capacity $k$ ($\text{Load Factor} = n / k$). When it exceeds a threshold (e.g., $0.75$), rehashing occurs to double table size.

### Q2: What are the two primary Collision Resolution Techniques?
**Answer:**
1. **Chaining (Separate Chaining):** Each array bucket contains a linked list (or balanced binary tree) storing all key-value pairs that hash to that same index.
2. **Open Addressing:** All elements are stored directly in the table array. On collision, search for another empty slot using **Linear Probing** ($i + 1$), **Quadratic Probing** ($i + c_1k + c_2k^2$), or **Double Hashing**.

### Q3: What is the Average vs Worst Case time complexity of HashMap operations?
**Answer:**
- **Average Case:** $O(1)$ for Search, Insert, and Delete.
- **Worst Case:** $O(n)$ if all keys hash to the same bucket index (hash collision flood). Note: Java 8+ mitigates this to $O(\log n)$ by switching long chains to Red-Black trees.

### Q4: What is the difference between `HashSet` and `HashMap`?
**Answer:**
- **`HashMap`:** Stores key-value pairs (`Map<K, V>`), keys must be unique, values can be duplicated.
- **`HashSet`:** Stores unique elements (`Set<E>`). Internally implemented using a `HashMap` where elements act as keys paired with a dummy object value.

### Q5: Can custom objects be used as HashMap keys? What are the requirements?
**Answer:**
Yes, but you **must override both `hashCode()` and `equals()`** methods.
- If two objects are equal according to `equals()`, they **must produce the same `hashCode()`**.
- Objects used as keys must be **immutable** so their hash code does not change after insertion.

---

## ⚠️ Beginner Pitfalls & Common Mistakes

1. **Worst Case Performance:**
   - In rare situations where your hash function distributes all keys to the same bucket index, a HashMap's lookup degrades from $O(1)$ to $O(n)$. Java 8 resolves this by converting collision linked lists into Red-Black trees when a list's length exceeds 8, keeping worst-case lookup at $O(\log n)$.

2. **Modifying Keys While inside the Map:**
   - Never modify an object after using it as a key in a HashMap. Doing so changes the object's hash code, making it impossible for the HashMap to locate it again, resulting in memory leaks and bugs.

---

> 👉 Next, open `08-Prefix-Sum.md` to learn how precomputations unlock range query optimization! 💪

