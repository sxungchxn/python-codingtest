import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())
dp = [0] * 1000001  # 0번째 값은 배제, i가 1로가는데 까지 걸리는 최소 연산의 횟수

dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 1

if N >= 6:
    for i in range(6, N+1):
        dp[i] = dp[i - 1] + 1
        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i // 5] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[N])
