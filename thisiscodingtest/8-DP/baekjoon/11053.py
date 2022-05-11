import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())
nums = list(map(int, readline().split()))
dp = [1] * N  # 현재 숫자를 포함하는 가장 긴 증가하는 부분 수열의 길이
max_len = 1

for i in range(0, N):
    for j in range(0, i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    max_len = max(max_len, dp[i])

print(max_len)
