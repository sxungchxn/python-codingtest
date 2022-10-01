import math


def countPrimes(n: int) -> int:
    primes = [True for _ in range(n + 1)]  # 해당 숫자는 소수인지 아닌지를 판별
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    result = 0
    for is_prime in primes:
        if is_prime:
            result += 1
    print(primes)
    return result


countPrimes(10)
