import math

# 1이상의 자연수
m = int(input())
n = int(input())


# primes = [2]


# 소수X 2, 4, 6, 8, 9, 12


# 4 = 1x4, 2x2
# 6 = 2x3

# 12 = 2x6 3x4

# 42 = 2x21 3x14 6x7 ...

# 59 = 1x59

# 60 = 2x30 3x20 4x15 5x12 6x10

# 소수 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

min_prime = -1
sum = 0
is_divisible = False

for num in range(m, n+1):
    if num == 1:
        continue
    is_divisible = False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_divisible = True
            break
    if is_divisible is False:
        if min_prime == -1:
            min_prime = num
        else:
            min_prime = min(min_prime, num)
        sum += num

if min_prime == -1:
    print(min_prime)
else:
    print(sum)
    print(min_prime)
