def swap_by_value(x: int, y: int):
    # Integers in Python are immutable; rebinding x and y has no outer effect
    temp = x
    x = y
    y = temp

def swap_in_container(container: list, i: int, j: int):
    # In-place swap by mutating the shared container reference
    container[i], container[j] = container[j], container[i]

def main():
    a = 15
    b = 99
    print(f"Before swap: a = {a}, b = {b}")

    swap_by_value(a, b)
    print(f"After swap_by_value: a = {a}, b = {b} (no change)")

    # Swapping values in Python idiomatically
    a, b = b, a
    print(f"After idiomatic swap: a = {a}, b = {b} (swapped)")

    arr = [15, 99]
    swap_in_container(arr, 0, 1)
    print(f"After container in-place swap: arr = {arr}")

if __name__ == "__main__":
    main()
