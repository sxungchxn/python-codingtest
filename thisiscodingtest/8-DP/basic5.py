import sys


def readline():
    return sys.stdin.readline().rstrip()


N, M = map(int, readline().split())
dp = [-1] * 10001
bills = []
for _ in range(N):
    num = int(readline())
    bills.append(num)
    dp[num] = 1

for i in range(1, M+1):
    if dp[i] == -1:
        for bill in bills:
            if i - bill >= 1 and dp[i-bill] != -1:
                if dp[i] == -1:
                    dp[i] = dp[i-bill] + 1
                else:
                    dp[i] = min(dp[i], dp[i - bill] + 1)

print(dp[M])
