def compute_spf(n: int) -> list[int]:
    spf = list(range(n + 1))
    p = 2
    while p * p <= n:
        if spf[p] == p:
            for i in range(p * p, n + 1, p):
                if spf[i] == i:
                    spf[i] = p
        p += 1
    return spf

def factorize(x: int, spf: list[int]) -> list[int]:
    factors = []
    while x > 1:
        factors.append(spf[x])
        x //= spf[x]
    return factors

if __name__ == "__main__":
    spf = compute_spf(100)
    print("Prime factors of 84:", factorize(84, spf))
