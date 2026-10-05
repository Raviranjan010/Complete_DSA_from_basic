def is_armstrong(n: int) -> bool:
    if n < 0:
        return False
    digits = [int(c) for c in str(n)]
    k = len(digits)
    return sum(d**k for d in digits) == n

def is_palindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return x == rev or x == rev // 10

if __name__ == "__main__":
    print("153 is Armstrong?", is_armstrong(153))
    print("1221 is Palindrome?", is_palindrome(1221))
