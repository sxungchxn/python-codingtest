import sys


def readline():
    return sys.stdin.readline().rstrip()


N, K = map(int, readline().split())
temps = list(map(int, readline().split()))
sum = 0

# 0 ~ N-2, N-1

for i in range(K):
    sum += temps[i]

max_sum = sum

for i in range(0, N - K):
    sum -= temps[i]
    sum += temps[i + K]
    max_sum = max(max_sum, sum)

print(max_sum)
