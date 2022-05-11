import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())
nums = list(map(int, readline().split()))
dp = [0] * 100  # i 번째 까지 왔을 때 털 수 있는 최대 식량

dp[0] = nums[0]
dp[1] = max(dp[0], nums[1])
for i in range(2, N):
    dp[i] = max(dp[i-1], nums[i] + dp[i-2])

print(dp[N - 1])
