"""
002-pass-by-value-vs-reference: Python Call-by-Object-Reference Mechanics

In Python, all arguments are passed via "Call-by-Object-Reference" (call-by-sharing):
1. Immutable objects (int, float, str, tuple):
   Reassigning a parameter binds a new object locally; caller's variable is unaffected.
   Idiomatic swap: `a, b = b, a` (tuple packing & unpacking).
2. Mutable objects (list, dict, set, class instance):
   - Reassigning `param = new_obj` rebinds the local name; caller is unaffected.
   - Mutating in-place `param[i] = val` or `param.append()` mutates the shared object; caller sees changes.
3. Large structures: Python passes references in O(1) time without copying. Read-only
   guarantees are achieved idiomatically via tuples or views.
"""

def attempt_swap_immutable(x: int, y: int):
    """Rebinding local parameters has NO effect on the caller."""
    x, y = y, x

def swap_in_mutable_sequence(seq: list, i: int, j: int):
    """In-place mutation affects the shared heap object."""
    seq[i], seq[j] = seq[j], seq[i]

def reassign_container(seq: list):
    """Rebinding the parameter does NOT rebind the caller's reference."""
    seq = [999, 888]

def inspect_large_structure_zero_copy(data: tuple) -> int:
    """Passing large structures is O(1) zero-copy reference passing."""
    return len(data)

def main():
    a = 15
    b = 99

    # 1. Immutable types cannot be swapped via a mutating helper
    attempt_swap_immutable(a, b)
    assert a == 15 and b == 99

    # 2. Idiomatic Python swap via tuple packing/unpacking
    a, b = b, a
    assert a == 99 and b == 15

    # 3. Mutable sequence in-place mutation
    arr = [15, 99]
    swap_in_mutable_sequence(arr, 0, 1)
    assert arr == [99, 15]

    # 4. Parameter rebinding does not mutate caller's list
    reassign_container(arr)
    assert arr == [99, 15]

    # 5. Zero-copy large container passing
    large_tuple = tuple(range(100000))
    count = inspect_large_structure_zero_copy(large_tuple)
    assert count == 100000

    print("[Python] Call-by-object-reference mechanics verified successfully.")

if __name__ == "__main__":
    main()
