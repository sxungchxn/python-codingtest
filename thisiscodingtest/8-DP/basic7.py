import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())
pows = list(map(int, readline().split()))

dp = [1] * N
max_len = 1

for i in range(N):
    for j in range(i):
        if pows[i] < pows[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            max_len = max(max_len, dp[i])

print(max_len)
print(N - max_len)
