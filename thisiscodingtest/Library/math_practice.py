import math

print(math.factorial(5))


def gcd(a: int, b: int):
    mod = a % b
    while(mod > 0):
        a = b
        b = mod
        mod = a % b
    return b


def lcm(a, b):
    return a * b / gcd(a, b)


print(gcd(24, 32))
print(lcm(24, 32))
