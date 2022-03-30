import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())

nums = list(map(int, readline().split()))

sum = 0
maxsum = -1000

for num in nums:
    sum += num
    if sum > maxsum:
        maxsum = sum
    if sum < 0:
        sum = 0

print(maxsum)
