import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())

dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for n in range(3, N+1):
    dp[n] = (dp[n-1] + 2 * dp[n-2]) % 796796

print(dp[N])
