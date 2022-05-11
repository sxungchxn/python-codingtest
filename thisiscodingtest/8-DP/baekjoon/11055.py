import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())
nums = list(map(int, readline().split()))

# 현재 숫자를 포함하는 가장 큰 증가 부분 수열의 합
dp = [0] * 1001
max_val = nums[0]

for i in range(0, N):
    dp[i] = nums[i]
    for j in range(0, i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + nums[i])
    max_val = max(max_val, dp[i])

print(max_val)
