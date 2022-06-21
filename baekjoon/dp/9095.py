import sys

dp = [0] * 11
dp[0] = dp[1] = 1


def readline():
    return sys.stdin.readline().rstrip()


def answer(N):
    if dp[N] != 0:
        return dp[N]
    f1 = answer(N - 1) if N - 1 >= 0 else 0
    f2 = answer(N - 2) if N - 2 >= 0 else 0
    f3 = answer(N - 3) if N - 3 >= 0 else 0
    dp[N] = f1 + f2 + f3
    return dp[N]


T = int(readline())

for _ in range(T):
    N = int(readline())
    print(answer(N))
