import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())
divider = 15746

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for n in range(3, N+1):
    dp[n] = (dp[n-1] + dp[n-2]) % divider

print(dp[N])

# N = 1
# 1

# N = 2
# 00 11

# N = 3
# 001 100 111

# N = 4
# 0011 1001 1111
# 0000 1100
