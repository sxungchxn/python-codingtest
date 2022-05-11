import sys


def readline():
    return sys.stdin.readline().rstrip()


S = readline()
Q = int(readline())


dp = [[0 for _ in range(len(S))] for i in range(ord('a'), ord('z') + 1)]

for i in range(len(S)):
    for j in range(ord('a'), ord('z') + 1):
        alpha_idx = j - ord('a')
        alpha = chr(j)
        if i == 0:
            if S[i] == alpha:
                dp[alpha_idx][0] = 1
        else:
            if S[i] == alpha:
                dp[alpha_idx][i] = dp[alpha_idx][i-1] + 1
            else:
                dp[alpha_idx][i] = dp[alpha_idx][i-1]

for i in range(Q):
    alpha, left, right = readline().split()
    left = int(left)
    right = int(right)
    alpha_idx = ord(alpha) - ord('a')
    if left == 0:
        print(dp[alpha_idx][right])
    else:
        print(dp[alpha_idx][right] - dp[alpha_idx][left - 1])
