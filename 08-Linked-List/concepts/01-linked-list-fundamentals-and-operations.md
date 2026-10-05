# 06 — Linked List — Complete Notes

> **What You'll Learn**: Singly, Doubly, Circular linked lists; Fast-slow pointer; Reversal techniques; Cycle detection  
> **Prerequisites**: Arrays, Pointers (Topics 02, 00)  
> **Time Required**: 1.5 weeks (15-18 hours)  
> **Importance**: 🌟🌟🌟🌟🌟 (Very high in interviews)

---

## 1. What is a Linked List? (Real-World Analogy)

Imagine a **treasure hunt** where each clue tells you where to find the next clue:

```
Clue 1: "Go to position A" → [Data: 10 | Next: 📍A]
                                    ↓
Clue 2: "Go to position B" → [Data: 20 | Next: 📍B]
                                    ↓
Clue 3: "Go to position C" → [Data: 30 | Next: 📍C]
                                    ↓
Final Clue: "You found it!"  → [Data: 40 | Next: NULL]
```

**Linked List** = A chain of **nodes**, where each node contains:
- **Data**: The actual value
- **Next**: Pointer to the next node

**Key Difference from Arrays**:
- Arrays: Contiguous memory (all elements together)
- Linked Lists: Scattered memory (elements connected by pointers)

💡 **TRICK**: Think of linked lists as a **chain of paper clips** — each clip holds data and connects to the next!

---

## 2. Why Do We Need Linked Lists?

### Advantages over Arrays:
✅ **Dynamic size**: Grow/shrink as needed (no fixed size)  
✅ **Fast insertion/deletion**: O(1) if you have the pointer  
✅ **No memory waste**: Use exactly what you need  
✅ **No resizing overhead**: Unlike vectors  

### Disadvantages:
❌ **No random access**: Must traverse from head (O(n) access)  
❌ **Extra memory**: Each node stores pointer  
❌ **Cache unfriendly**: Nodes scattered in memory  

### Real-World Uses:
- Browser history (back/forward buttons)
- Undo/Redo in text editors
- Music playlist (next/previous song)
- Hash table collision handling (chaining)

---

## 3. Core Concepts & Terminology

### 3.1 Singly Linked List

```cpp
#include <iostream>
using namespace std;

// Node structure
struct Node {
    int data;        // Data part
    Node* next;      // Pointer to next node
    
    // Constructor
    Node(int val) {
        data = val;
        next = nullptr;
    }
};

// Visual: [10|→] → [20|→] → [30|→] → [40|NULL]
```

**Complete Implementation**:

```cpp
class LinkedList {
private:
    Node* head;  // Pointer to first node
    
public:
    LinkedList() {
        head = nullptr;  // Empty list initially
    }
    
    // Insert at beginning - O(1)
    void insertAtHead(int val) {
        Node* newNode = new Node(val);  // Create new node
        newNode->next = head;           // Point to current head
        head = newNode;                 // Update head
    }
    
    // Insert at end - O(n)
    void insertAtTail(int val) {
        Node* newNode = new Node(val);
        
        if(head == nullptr) {  // Empty list
            head = newNode;
            return;
        }
        
        Node* temp = head;
        while(temp->next != nullptr) {  // Traverse to end
            temp = temp->next;
        }
        temp->next = newNode;  // Link last node to new node
    }
    
    // Delete by value - O(n)
    void deleteNode(int val) {
        if(head == nullptr) return;
        
        // If head node itself holds the value
        if(head->data == val) {
            Node* temp = head;
            head = head->next;
            delete temp;
            return;
        }
        
        // Search for the node to delete
        Node* current = head;
        while(current->next != nullptr && current->next->data != val) {
            current = current->next;
        }
        
        // If value found
        if(current->next != nullptr) {
            Node* temp = current->next;
            current->next = current->next->next;  // Skip the node
            delete temp;
        }
    }
    
    // Search for element - O(n)
    bool search(int val) {
        Node* current = head;
        while(current != nullptr) {
            if(current->data == val) {
                return true;
            }
            current = current->next;
        }
        return false;
    }
    
    // Print list
    void print() {
        Node* temp = head;
        while(temp != nullptr) {
            cout << temp->data << " → ";
            temp = temp->next;
        }
        cout << "NULL" << endl;
    }
    
    // Destructor - Free memory
    ~LinkedList() {
        Node* current = head;
        while(current != nullptr) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }
};

int main() {
    LinkedList ll;
    
    ll.insertAtTail(10);
    ll.insertAtTail(20);
    ll.insertAtHead(5);
    ll.insertAtTail(30);
    
    cout << "List: ";
    ll.print();  // 5 → 10 → 20 → 30 → NULL
    
    ll.deleteNode(20);
    cout << "After deleting 20: ";
    ll.print();  // 5 → 10 → 30 → NULL
    
    cout << "Search 10: " << (ll.search(10) ? "Found" : "Not Found") << endl;
    
    return 0;
}
```

---

## 4. Visual Diagram: Linked List Operations

```
┌─────────────────────────────────────────────────────────────┐
│              LINKED LIST OPERATIONS                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. INSERT AT HEAD (O(1))                                   │
│     New Node(5) → [10|→] → [20|→] → NULL                   │
│          ↓                                                   │
│     head points to new node                                  │
│                                                              │
│  2. INSERT AT TAIL (O(n))                                   │
│     [10|→] → [20|→] → New Node(30)                          │
│          Traverse to end, then link                          │
│                                                              │
│  3. DELETE NODE (O(n))                                      │
│     [10|→] → [20|→] → [30|→]                                │
│          ↓ Skip 20                                           │
│     [10|───────────→] → [30|→]                              │
│                                                              │
│  4. REVERSE LIST                                            │
│     Before: [10|→] → [20|→] → [30|NULL]                     │
│     After:  [30|→] → [20|→] → [10|NULL]                     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. Essential Linked List Patterns

### Pattern 1: Reverse Linked List

```cpp
// Iterative reversal - O(n) time, O(1) space
Node* reverseList(Node* head) {
    Node* prev = nullptr;
    Node* current = head;
    Node* next = nullptr;
    
    while(current != nullptr) {
        next = current->next;      // Store next node
        current->next = prev;      // Reverse the link
        prev = current;            // Move prev forward
        current = next;            // Move current forward
    }
    
    return prev;  // New head
}
```

**Dry Run**:
```
Original: 1 → 2 → 3 → NULL

Iteration 1:
prev = NULL, current = 1, next = 2
1 → NULL (reversed)

Iteration 2:
prev = 1, current = 2, next = 3
2 → 1 → NULL

Iteration 3:
prev = 2, current = 3, next = NULL
3 → 2 → 1 → NULL ✓

Result: 3 → 2 → 1 → NULL
```

---

### Pattern 2: Detect Cycle (Floyd's Algorithm)

**Analogy**: Two runners on a track — faster runner will eventually lap the slower one!

```cpp
// Floyd's Cycle Detection - O(n) time, O(1) space
bool hasCycle(Node* head) {
    Node* slow = head;  // Moves 1 step
    Node* fast = head;  // Moves 2 steps
    
    while(fast != nullptr && fast->next != nullptr) {
        slow = slow->next;           // Move slow by 1
        fast = fast->next->next;     // Move fast by 2
        
        if(slow == fast) {
            return true;  // Cycle detected!
        }
    }
    
    return false;  // No cycle
}
```

**Visualization**:
```
List with cycle: 1 → 2 → 3 → 4 → 5
                      ↑         ↓
                      ← 6 ← 7 ←

Step 0: slow=1, fast=1
Step 1: slow=2, fast=3
Step 2: slow=3, fast=5
Step 3: slow=4, fast=4 ← MEET! Cycle detected ✓
```

💡 **TRICK**: **Floyd's Mnemonic**: "Tortoise and Hare" — if there's a cycle, the hare catches the tortoise!

---

### Pattern 3: Find Middle Element

```cpp
// Find middle using fast-slow pointers - O(n) time
Node* findMiddle(Node* head) {
    Node* slow = head;
    Node* fast = head;
    
    while(fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    return slow;  // Middle node
}
```

**Why it works**: When fast reaches end (2x speed), slow is at middle!

---

### Pattern 4: Merge Two Sorted Lists

```cpp
// Merge two sorted linked lists - O(n+m) time
Node* mergeTwoLists(Node* l1, Node* l2) {
    // Create dummy node
    Node* dummy = new Node(0);
    Node* current = dummy;
    
    while(l1 != nullptr && l2 != nullptr) {
        if(l1->data <= l2->data) {
            current->next = l1;
            l1 = l1->next;
        } else {
            current->next = l2;
            l2 = l2->next;
        }
        current = current->next;
    }
    
    // Attach remaining nodes
    if(l1 != nullptr) current->next = l1;
    if(l2 != nullptr) current->next = l2;
    
    return dummy->next;
}
```

---

## 6. Doubly Linked List

Each node has **two pointers**: previous and next!

```cpp
struct DoublyNode {
    int data;
    DoublyNode* prev;
    DoublyNode* next;
    
    DoublyNode(int val) {
        data = val;
        prev = nullptr;
        next = nullptr;
    }
};

// Visual: NULL ← [10|↔] ↔ [20|↔] ↔ [30|↔] → NULL
```

**Advantage**: Can traverse both directions!

---

## 7. All Operations with Time & Space Complexity

| Operation | Singly LL | Doubly LL | Array |
|-----------|-----------|-----------|-------|
| Access by index | O(n) | O(n) | O(1) |
| Search | O(n) | O(n) | O(n) |
| Insert at head | O(1) | O(1) | O(n) |
| Insert at tail | O(n) | O(1) with tail ptr | O(1) |
| Delete by value | O(n) | O(n) | O(n) |
| Insert after node | O(1) | O(1) | O(n) |

---

## 8. Common Patterns & Tricks

### 💡 TRICK 1: Dummy Node Pattern
```cpp
// Simplifies edge cases
Node* dummy = new Node(0);
dummy->next = head;
// Work with dummy->next
```

### 💡 TRICK 2: Two Pointer Techniques
```cpp
// Find nth node from end
Node* fast = head;
for(int i = 0; i < n; i++) fast = fast->next;

Node* slow = head;
while(fast != nullptr) {
    slow = slow->next;
    fast = fast->next;
}
return slow;  // nth from end
```

---

## 9-13. [Complete sections with more examples, dry runs, MCQs, interview questions]

---

**🎉 Congratulations! You've mastered Linked Lists!**

**Next Steps**:
1. ✅ Complete MCQs in `06_mcqs.md`
2. ✅ Solve 20 linked list problems
3. ✅ Move to **07_Stack**

[← Back to README](../README.md) | [Next: Stack →](../../09-Stack-and-Queue/concepts/01-stack-fundamentals-and-monotonic-stack.md)


---

## Supplementary Notes from 10-Linked-List.md

# 🔗 10 — Linked List

> **Explain Like I'm 5:** Think of a train. Each train coach (called a **Node**) carries some cargo (the value) and is coupled to the **next** coach via a link. You cannot jump directly to coach 5 — you must walk from the engine, coach by coach. That's a Linked List!
>
> ```
> [ 10 | • ] ──► [ 20 | • ] ──► [ 30 | • ] ──► NULL (end of train)
>   val next       val next       val next
>  (head)
> ```

---

## 🧠 Memory Layout: Arrays vs. Linked Lists

To understand why we need Linked Lists, let's compare how they reside in RAM compared to Arrays:

| Feature | Arrays | Linked Lists |
| :--- | :--- | :--- |
| **Memory Allocation** | Contiguous (one single block in RAM) | Scattered (individual blocks in Heap memory) |
| **Random Access** | $O(1)$ (Using index offset arithmetic) | $O(n)$ (Must traverse element by element) |
| **Insert / Delete at End** | $O(1)$ amortized | $O(n)$ (without tail pointer) or $O(1)$ (with tail pointer) |
| **Insert / Delete at Start**| $O(n)$ (Requires shifting all elements) | $O(1)$ (Only swap a few pointers) |
| **Cache Locality** | Highly cache-friendly (spatial locality) | Poor cache-friendliness (scattered references) |

### Visualizing Linked List Memory Scattering
In a Linked List, nodes are allocated anywhere in Heap memory. They contain a pointer/reference variable storing the address of the next node:

```
HEAP ADDRESSES:

Address 0x1048: Node [ Val: 10 | Next: 0x2090 ] ─────┐
                                                      │
Address 0x10B4: Node [ Val: 30 | Next: NULL   ] ◄─────┼─────┐
                                                      │     │
Address 0x2090: Node [ Val: 20 | Next: 0x10B4 ] ◄─────┘     │
                                                            │
Logical Flow:   Head (0x1048) ──► Node (0x2090) ──► Node (0x10B4) ──► NULL
```

---

## 🛠️ The Node Class Definition

Here is how a Node is defined in Java, Python, and C++:

<details>
<summary>💻 Node Class Implementations</summary>

### Java
```java
public class ListNode {
    public int val;
    public ListNode next;
    
    public ListNode(int val) {
        this.val = val;
        this.next = null;
    }
}
```

### Python
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### C++
```cpp
struct ListNode {
    int val;
    ListNode* next;
    
    ListNode(int x) : val(x), next(nullptr) {}
};
```
</details>

---

## 📋 The Interview Pattern Cheat-Sheet

| Pattern | Description | Key Mechanism |
| :--- | :--- | :--- |
| **Traversal** | Move sequentially through the list. | `curr = curr.next` |
| **Fast & Slow** | Pointers moving at different speeds. | `slow = slow.next`, `fast = fast.next.next` |
| **Pointer Flip** | Reversing node linkages. | `next = curr.next; curr.next = prev; prev = curr; curr = next;` |
| **Dummy Node** | A fake node pointing to the head. | Eliminates head deletion/insertion edge cases. |

---

## 🟢 Day 1: Foundational Pointers

These problems form the building blocks of all linked list manipulations.

### Solution 4: Middle of the Linked List

**Intuition:** 
Use a slow pointer and a fast pointer.
- `slow` moves 1 step at a time.
- `fast` moves 2 steps at a time.
When `fast` reaches the end (`null` or `fast.next` is `null`), `slow` will be exactly at the middle node.

**Complexity:**
- **Time:** $O(n)$ — Single pass traversal.
- **Space:** $O(1)$ — Two pointer variables.

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public ListNode middleNode(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;        // 1 step
        fast = fast.next.next;   // 2 steps
    }
    return slow;
}
```

#### Python
```python
def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next        # 1 step
        fast = fast.next.next   # 2 steps
    return slow
```

#### C++
```cpp
ListNode* middleNode(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;       // 1 step
        fast = fast->next->next; // 2 steps
    }
    return slow;
}
```
</details>

---

### Solution 5: Reverse Linked List

**Intuition:**
We reverse the linkages of the nodes in-place. We need three pointers:
- `prev`: The node behind our current pointer (starts as `null`).
- `curr`: Our current pointer (starts as `head`).
- `next`: Temporarily stores the node ahead of us before we flip pointers.

```
Execution Loop (Save -> Flip -> Move -> Move):
1. next = curr.next   (Save next node)
2. curr.next = prev   (Flip pointer backward)
3. prev = curr        (Move prev forward)
4. curr = next        (Move curr forward)
```

**Complexity:**
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode curr = head;
    while (curr != null) {
        ListNode next = curr.next; // 1. Save what's ahead
        curr.next = prev;          // 2. Flip connection backward
        prev = curr;               // 3. Move prev up
        curr = next;               // 4. Move curr up
    }
    return prev; // prev ends up pointing to the new head
}
```

#### Python
```python
def reverseList(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next   # 1. Save what's ahead
        curr.next = prev  # 2. Flip connection backward
        prev = curr       # 3. Move prev up
        curr = nxt        # 4. Move curr up
    return prev
```

#### C++
```cpp
ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* curr = head;
    while (curr) {
        ListNode* next = curr->next; // 1. Save what's ahead
        curr->next = prev;           // 2. Flip connection backward
        prev = curr;                 // 3. Move prev up
        curr = next;                 // 4. Move curr up
    }
    return prev;
}
```
</details>

---

### Solution 6: Linked List Cycle (Floyd's Cycle Finding Algorithm)

**Intuition:**
If there is a cycle, a fast pointer moving 2 steps at a time will eventually meet a slow pointer moving 1 step at a time inside the loop (like a fast runner lapping a slow runner on a track). If there is no cycle, `fast` will hit `null`.

**Complexity:**
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public boolean hasCycle(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) {
            return true; // Met -> Cycle exists
        }
    }
    return false; // Reached end -> No cycle
}
```

#### Python
```python
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

#### C++
```cpp
bool hasCycle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            return true;
        }
    }
    return false;
}
```
</details>

---

## 🟡 Day 2: Interview Combinations

These problems combine Day 1 skills to solve complex scenarios.

### Solution 7: Remove Nth Node From End of List

**Intuition:**
We need to remove the $N$-th node from the end. 
- Use a `dummy` node pointing to the head.
- Place `slow` and `fast` pointers at `dummy`.
- Move `fast` forward by $N + 1$ steps. This establishes a gap of size $N$ between `slow` and `fast`.
- Move both together at the same speed. When `fast` reaches `null`, `slow` will point to the node **just before** the target.
- Perform insertion deletion: `slow.next = slow.next.next`.

**Complexity:**
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode slow = dummy;
    ListNode fast = dummy;
    
    // Step 1: Move fast pointer N+1 steps forward
    for (int i = 0; i <= n; i++) {
        fast = fast.next;
    }
    
    // Step 2: Move both together until fast reaches null
    while (fast != null) {
        slow = slow.next;
        fast = fast.next;
    }
    
    // Step 3: Delete node
    slow.next = slow.next.next;
    return dummy.next;
}
```

#### Python
```python
def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy
    
    for _ in range(n + 1):
        fast = fast.next
        
    while fast:
        slow = slow.next
        fast = fast.next
        
    slow.next = slow.next.next
    return dummy.next
```

#### C++
```cpp
ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode* dummy = new ListNode(0);
    dummy->next = head;
    ListNode* slow = dummy;
    ListNode* fast = dummy;
    
    for (int i = 0; i <= n; i++) {
        fast = fast->next;
    }
    
    while (fast) {
        slow = slow->next;
        fast = fast->next;
    }
    
    slow->next = slow->next->next;
    ListNode* result = dummy->next;
    delete dummy; // Clean heap allocation
    return result;
}
```
</details>

---

### Solution 8: Merge Two Sorted Lists

**Complexity:**
- **Time:** $O(n + m)$
- **Space:** $O(1)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    ListNode dummy = new ListNode(0);
    ListNode tail = dummy;
    
    while (list1 != null && list2 != null) {
        if (list1.val <= list2.val) {
            tail.next = list1;
            list1 = list1.next;
        } else {
            tail.next = list2;
            list2 = list2.next;
        }
        tail = tail.next;
    }
    
    // Attach remainder nodes
    tail.next = (list1 != null) ? list1 : list2;
    return dummy.next;
}
```

#### Python
```python
def mergeTwoLists(list1, list2):
    dummy = ListNode(0)
    tail = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
        
    tail.next = list1 if list1 else list2
    return dummy.next
```

#### C++
```cpp
ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    
    while (list1 && list2) {
        if (list1->val <= list2->val) {
            tail->next = list1;
            list1 = list1->next;
        } else {
            tail->next = list2;
            list2 = list2->next;
        }
        tail = tail->next;
    }
    
    tail->next = list1 ? list1 : list2;
    return dummy.next;
}
```
</details>

---

### Solution 9: Add Two Numbers

**Complexity:**
- **Time:** $O(\max(n, m))$
- **Space:** $O(\max(n, m))$ to construct the result list.

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode dummy = new ListNode(0);
    ListNode tail = dummy;
    int carry = 0;
    
    while (l1 != null || l2 != null || carry > 0) {
        int sum = carry;
        if (l1 != null) {
            sum += l1.val;
            l1 = l1.next;
        }
        if (l2 != null) {
            sum += l2.val;
            l2 = l2.next;
        }
        
        tail.next = new ListNode(sum % 10);
        carry = sum / 10;
        tail = tail.next;
    }
    return dummy.next;
}
```

#### Python
```python
def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val = carry
        if l1:
            val += l1.val
            l1 = l1.next
        if l2:
            val += l2.val
            l2 = l2.next
            
        tail.next = ListNode(val % 10)
        carry = val // 10
        tail = tail.next
        
    return dummy.next
```

#### C++
```cpp
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode* dummy = new ListNode(0);
    ListNode* tail = dummy;
    int carry = 0;
    
    while (l1 || l2 || carry) {
        int sum = carry;
        if (l1) {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2) {
            sum += l2->val;
            l2 = l2->next;
        }
        tail->next = new ListNode(sum % 10);
        carry = sum / 10;
        tail = tail->next;
    }
    return dummy->next;
}
```
</details>

---

### Solution 10: Linked List Cycle II

**Intuition:**
1. Run Floyd's algorithm to detect if a cycle exists. Let the meeting point of `slow` and `fast` be node $M$.
2. Reset `slow` back to `head`. Keep `fast` at meeting point $M$.
3. Move both pointers forward 1 step at a time. The node where they meet is the start of the cycle.
*(Proof: Let distance from head to cycle start be $D$. Let cycle length be $C$. The distance from cycle start to meeting point is $K$. The math shows that $D = x \cdot C - K$, which means the distance from head to cycle start is congruent to the distance from the meeting point to cycle start).*

**Complexity:**
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public ListNode detectCycle(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;
    
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) {
            // Cycle detected. Find start node.
            slow = head;
            while (slow != fast) {
                slow = slow.next;
                fast = fast.next;
            }
            return slow; // Start of cycle
        }
    }
    return null; // No cycle
}
```

#### Python
```python
def detectCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
```

#### C++
```cpp
ListNode* detectCycle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            slow = head;
            while (slow != fast) {
                slow = slow->next;
                fast = fast->next;
            }
            return slow;
        }
    }
    return nullptr;
}
```
</details>

---

### Solution 11: Palindrome Linked List

**Intuition:**
1. Find the middle of the list using slow/fast pointers.
2. Reverse the second half of the list starting from the middle node.
3. Compare the values of the first half (from `head`) and the reversed second half.

**Complexity:**
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public boolean isPalindrome(ListNode head) {
    // 1. Find middle
    ListNode slow = head;
    ListNode fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    
    // 2. Reverse second half
    ListNode prev = null;
    ListNode curr = slow;
    while (curr != null) {
        ListNode next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    
    // 3. Compare halves
    ListNode left = head;
    ListNode right = prev;
    while (right != null) {
        if (left.val != right.val) {
            return false;
        }
        left = left.next;
        right = right.next;
    }
    return true;
}
```

#### Python
```python
def isPalindrome(head):
    # 1. Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # 2. Reverse second half
    prev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
    # 3. Compare halves
    left = head
    right = prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
```

#### C++
```cpp
bool isPalindrome(ListNode* head) {
    // 1. Find middle
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    // 2. Reverse second half
    ListNode* prev = nullptr;
    ListNode* curr = slow;
    while (curr) {
        ListNode* next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    
    // 3. Compare halves
    ListNode* left = head;
    ListNode* right = prev;
    while (right) {
        if (left->val != right->val) return false;
        left = left->next;
        right = right->next;
    }
    return true;
}
```
</details>

---

### Solution 12: Odd Even Linked List

**Intuition:**
We create two separate chains: one for nodes at odd indices, one for nodes at even indices.
- Initialize `odd = head` and `even = head.next`.
- Store `evenHead = even` to connect the end of the odd chain to the beginning of the even chain later.
- Loop and decouple nodes:
  `odd.next = even.next; odd = odd.next;`
  `even.next = odd.next; even = even.next;`
- Conclude by linking `odd.next = evenHead`.

**Complexity:**
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public ListNode oddEvenList(ListNode head) {
    if (head == null) return null;
    ListNode odd = head;
    ListNode even = head.next;
    ListNode evenHead = even;
    
    while (even != null && even.next != null) {
        odd.next = even.next;
        odd = odd.next;
        even.next = odd.next;
        even = even.next;
    }
    odd.next = evenHead;
    return head;
}
```

#### Python
```python
def oddEvenList(head):
    if not head:
        return None
    odd = head
    even = head.next
    even_head = even
    
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
        
    odd.next = even_head
    return head
```

#### C++
```cpp
ListNode* oddEvenList(ListNode* head) {
    if (!head) return nullptr;
    ListNode* odd = head;
    ListNode* even = head->next;
    ListNode* evenHead = even;
    
    while (even && even->next) {
        odd->next = even->next;
        odd = odd->next;
        even->next = odd->next;
        even = even->next;
    }
    odd->next = evenHead;
    return head;
}
```
</details>

<details>
<summary>📋 Step-by-Step Dry Run</summary>

Input: `head = [1, 2, 3, 4, 5]`

- Initial pointers: `odd` $\to 1$, `even` $\to 2$, `evenHead` $\to 2$
- **Iteration 1 (`even = 2`):**
  - `odd.next = even.next` (3) $\implies$ `odd` chain: $1 \to 3$
  - `odd = 3`
  - `even.next = odd.next` (4) $\implies$ `even` chain: $2 \to 4$
  - `even = 4`
- **Iteration 2 (`even = 4`):**
  - `odd.next = even.next` (5) $\implies$ `odd` chain: $1 \to 3 \to 5$
  - `odd = 5`
  - `even.next = odd.next` (`null`) $\implies$ `even` chain: $2 \to 4 \to \text{null}$
  - `even = null`
- Loop terminates (`even == null`).
- Connect chains: `odd.next = evenHead` ($5 \to 2$).

**Result:** `[1, 3, 5, 2, 4]` ✅
</details>

---

## 🎓 Viva Questions & Answers

### Q1: What is the primary difference in memory allocation between Arrays and Linked Lists?
**Answer:**
- **Array:** Continuous block of memory allocated contiguously. Size is fixed (or requires re-allocation), and random access is $O(1)$.
- **Linked List:** Dynamic nodes scattered non-contiguously in Heap memory connected by reference pointers. Insertion/deletion is $O(1)$ if pointer reference is known, but element access is $O(n)$.

### Q2: What is a Dummy Head Pointer Node, and why is it useful?
**Answer:**
A **Dummy Node** is a placeholder node (`ListNode dummy = new ListNode(0)`) placed before `head`. It simplifies code by eliminating edge cases when inserting or deleting at the very beginning of the list, allowing uniform pointer operations. `dummy.next` returns the modified actual head.

### Q3: Why is Floyd's Cycle Detection algorithm guaranteed to find a cycle if one exists?
**Answer:**
Let the fast pointer move 2 steps and slow pointer move 1 step. In each step, the distance between `fast` and `slow` inside the cycle decreases by $1$ node ($(2 - 1) = 1$). If the cycle length is $C$, `fast` will catch up to `slow` in at most $C$ steps after both enter the cycle.

### Q4: Compare Singly Linked List vs Doubly Linked List vs Circular Linked List.
**Answer:**
- **Singly Linked List:** Each node has a `val` and `next` pointer. Uses less memory per node, but can only traverse forward.
- **Doubly Linked List:** Each node has `val`, `next`, and `prev` pointers. Allows bi-directional traversal and $O(1)$ deletion given node reference, but uses extra pointer memory.
- **Circular Linked List:** Tail node's `next` points back to `head` (or head's `prev` points to tail). Useful for round-robin scheduling algorithms.

### Q5: How do you reverse a Singly Linked List in $O(n)$ time and $O(1)$ space?
**Answer:**
Maintain three pointers: `prev = null`, `curr = head`, and `next = null`.
In a loop while `curr != null`:
1. Save `next = curr.next`.
2. Reverse link: `curr.next = prev`.
3. Advance: `prev = curr`, `curr = next`.
Return `prev` as the new head.

---

## ⚠️ Beginner Pitfalls & Common Mistakes

1. **Null Pointer Exceptions (Dereferencing Null):**
   - The #1 source of crashes in linked list code.
   - Doing `curr = curr.next` when `curr` is `null` will throw a crash.
   - Doing `fast.next.next` when `fast` is `null` or `fast.next` is `null` will throw a crash. Always write bounds guard checks first: `while (fast != null && fast.next != null)`.

2. **Pointer Loss (The Orphan Trap):**
   - If you do `head.next = prev` without saving the original `head.next` pointer first, you sever the link to the rest of the list. That remaining list gets orphaned in memory.
   - **Rule:** Always record pointers to variables *before* you overwrite them.

---

> 👉 Next, open `11-Stack.md` to explore LIFO stack operations! 💪

