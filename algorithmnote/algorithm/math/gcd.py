# a와 b의 최대 공약수 == b와 a%b의 최대공약수

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


print(gcd(5, 2))
