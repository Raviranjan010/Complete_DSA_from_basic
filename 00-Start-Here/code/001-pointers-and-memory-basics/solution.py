"""
001-pointers-and-memory-basics: Python Reference Semantics, Object Identity & GC

In Python, there are NO raw memory pointers or pointer arithmetic.
Instead, Python uses:
1. Object References: Every variable is a name bound to an object in heap memory.
2. Object Identity (id()): Represents the memory address of the object in CPython.
3. Mutability vs Immutability:
   - Immutable objects (int, float, str, tuple): cannot be changed in place.
   - Mutable objects (list, dict, custom classes): state can be mutated via any reference.
4. Garbage Collection: Python uses reference counting + generational cyclic GC.
"""

import sys
import gc

class Entity:
    """A custom class demonstrating reference binding and field mutation."""
    def __init__(self, value: int):
        self.value = value

def demonstrate_object_identity():
    # 1. Names and Object Identity
    val1 = 1000
    val2 = val1
    assert val1 is val2
    assert id(val1) == id(val2)

    # 2. Immutability: Rebinding does NOT mutate the original object
    val2 += 1
    assert val1 == 1000 and val2 == 1001
    assert val1 is not val2

    # 3. Mutable Objects: Multiple references observe the same mutation
    entity1 = Entity(10)
    entity2 = entity1  # Both names point to the same object reference
    assert entity1 is entity2
    assert id(entity1) == id(entity2)

    entity2.value = 42
    assert entity1.value == 42  # Reflected through entity1

    # 4. Traversal: List holds references to objects, not raw contiguous memory
    items = [Entity(10), Entity(20), Entity(30)]
    for i, item in enumerate(items):
        assert item.value == (i + 1) * 10
        assert isinstance(id(item), int)

    # 5. Reference Counting and Garbage Collection
    initial_refs = sys.getrefcount(entity1)
    alias = entity1
    assert sys.getrefcount(entity1) == initial_refs + 1
    del alias
    assert sys.getrefcount(entity1) == initial_refs

    print("[Python] Object identity, reference semantics, and GC verified successfully.")

if __name__ == "__main__":
    demonstrate_object_identity()
