"""
003-array-decay-and-dynamic-allocation: Python Dynamic Lists & Memory Model

In Python, there is NO array decay:
1. Lists are dynamic arrays of object references allocated on the heap.
2. The length is permanently stored in the PyVarObject header (`ob_size`).
   `len(lst)` is O(1) and is never lost across function calls.
3. Over-allocation: CPython uses an amortized geometric growth pattern
   (0, 4, 8, 16, 25, 35, 46, ...) during `append()`.
4. Garbage Collection: Python reclaims memory automatically when reference count drops to 0.
"""

import sys

def inspect_list(elements: list) -> int:
    # Length metadata is preserved across all function boundaries
    return len(elements)

def demonstrate_dynamic_list():
    elements = [10, 20, 30, 40, 50]
    
    # 1. No array decay: length is preserved
    assert len(elements) == 5
    assert inspect_list(elements) == 5

    # 2. Container memory overhead (PyListObject header + pointer array)
    base_size = sys.getsizeof(elements)
    assert base_size > 0

    # 3. Dynamic resizing via geometric over-allocation
    dynamic_list = []
    sizes = []
    for i in range(20):
        dynamic_list.append(i)
        sizes.append(sys.getsizeof(dynamic_list))
    
    # Over-allocation causes jump steps rather than reallocating every append
    assert len(set(sizes)) > 1

    print("[Python] Dynamic array internals and lack of array decay verified successfully.")

if __name__ == "__main__":
    demonstrate_dynamic_list()
