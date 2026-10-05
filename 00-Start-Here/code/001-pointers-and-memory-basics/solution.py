def demonstrate_reference_basics():
    # Python uses reference semantics and object IDs (memory-like address equivalent)
    target = [10]  # Mutable container to demonstrate indirect modification
    ref = target

    print(f"Initial scalar value: {ref[0]}")
    print(f"Memory id of container: {hex(id(target))}")

    # Indirect modification
    ref[0] = 42
    print(f"Modified scalar value via reference: {target[0]}")

    # Simulating array memory traversal
    arr = [10, 20, 30]
    print("\nTraversing list via index and object identity:")
    for i, val in enumerate(arr):
        print(f"Index {i}: Object ID = {hex(id(val))} | Value = {val}")

if __name__ == "__main__":
    demonstrate_reference_basics()
