def power(base: int, exp: int, mod: int = 10**9 + 7) -> int:
    res = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return res

if __name__ == "__main__":
    print(f"2^10 mod 1e9+7 = {power(2, 10)}")
