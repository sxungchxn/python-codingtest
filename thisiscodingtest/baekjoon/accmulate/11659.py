import sys


def readline():
    return sys.stdin.readline().rstrip()


N, M = map(int, readline().split())
nums = list(map(int, readline().split()))

prefix = [0] * N
prefix[0] = nums[0]

for i in range(1, N):
    prefix[i] = prefix[i - 1] + nums[i]

for _ in range(M):
    n, m = map(int, readline().split())
    print(prefix[m - 1] - prefix[n-1] + nums[n-1])
