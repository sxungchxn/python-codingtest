import sys

dp = [0] * 1001
dp[0] = 1


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())

for i in range(1, N + 1):
    f1 = dp[i - 1] if i - 1 >= 0 else 0
    f2 = dp[i - 2] if i - 2 >= 0 else 0
    dp[i] = (f1 + f2) % 10007

print(dp[N] % 10007)
