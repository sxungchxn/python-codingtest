import sys


def readline():
    return sys.stdin.readline().rstrip()


DEFAULT = 99999
N = int(readline())

dp = [DEFAULT] * 50001
sqs = []

i = 1
while i * i <= N:
    sq = i * i
    dp[sq] = 1
    sqs.append(sq)
    i += 1


for i in range(1, N+1):
    if dp[i] == DEFAULT:
        for sq in sqs:
            if sq >= i:
                break
            if dp[i] <= 2:
                break
            dp[i] = min(dp[i], dp[sq] + dp[i - sq])


print(dp[N])

# 1 4 9 16 25 36 49 64 81 ... = 1
# dp[1] = 1
# dp[2] = 1 + 1 = 2
# dp[3] = 2 + 1 = 3
# dp[4] = 1
# dp[5] = dp[4] + dp[1] = 2
# dp[6] = 3

# dp[7] = dp[4] + dp[3], dp[1] + dp[6] = 3

# ..
# dp[26] = dp[1] + dp[25], dp[9] + dp[16]

# 36 = 1 + 35, 4 + 32, 9 + 27, 16 + 20, 25 + 11
# 37 = 1 + 36, 4 + 33, 9 + 28, 16 + 21, 25 + 12,
