MOD = 10**9 + 7

def power(base: int, exp: int) -> int:
    return pow(base, exp, MOD)

def mod_inverse(n: int) -> int:
    return power(n, MOD - 2)

def mod_divide(a: int, b: int) -> int:
    return (a % MOD * mod_inverse(b)) % MOD

if __name__ == "__main__":
    print(f"14 / 2 mod 1e9+7 = {mod_divide(14, 2)}")
