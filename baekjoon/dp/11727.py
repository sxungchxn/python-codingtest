import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())

dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1

# dp[n] = dp[n-1] + dp[n-2] * 2
for i in range(2, N+1):
    dp[i] = (dp[i - 1] % 10007 + (dp[i - 2] * 2) % 10007) % 10007

print(dp[N])
