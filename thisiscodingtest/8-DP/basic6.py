import sys


def readline():
    return sys.stdin.readline().rstrip()


T = int(readline())

# N = 3, M = 4

# 1 3 3 2
# 2 1 4 1
# 0 6 4 7

for _ in range(T):
    N, M = map(int, readline().split())
    nums = [[0 for col in range(M)] for row in range(N)]
    dp = [[0 for col in range(M)] for row in range(N)]
    inputs = list(map(int, readline().split()))
    for i in range(N):
        for j in range(M):
            nums[i][j] = inputs[i * M + j]
    for j in range(M):
        if j == 0:
            for i in range(N):
                dp[i][j] = nums[i][j]
        else:
            for i in range(N):
                if i == 0:
                    dp[i][j] = nums[i][j] + max(dp[i][j - 1], dp[i+1][j-1])
                elif i == N - 1:
                    dp[i][j] = nums[i][j] + max(dp[i-1][j-1], dp[i][j-1])
                else:
                    dp[i][j] = nums[i][j] + \
                        max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
    result = dp[0][M-1]
    for i in range(1, N):
        result = max(result, dp[i][M-1])
    print(result)
