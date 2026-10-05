def sieve(n: int) -> list[bool]:
    if n < 2:
        return [False] * (n + 1)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime

if __name__ == "__main__":
    limit = 30
    primes = sieve(limit)
    print("Primes up to 30:", [i for i in range(2, limit + 1) if primes[i]])
