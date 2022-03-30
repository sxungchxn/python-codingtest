def gcd(a, b):
    if a % b == 0:
        return a
    return gcd(b, a % b)


print(gcd(5, 2))
