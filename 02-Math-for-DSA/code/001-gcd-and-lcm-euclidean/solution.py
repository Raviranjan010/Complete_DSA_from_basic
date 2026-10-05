import math

def compute_gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def compute_lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return (a // compute_gcd(a, b)) * b

if __name__ == "__main__":
    a, b = 48, 18
    print(f"GCD({a}, {b}) = {compute_gcd(a, b)}")
    print(f"LCM({a}, {b}) = {compute_lcm(a, b)}")
