import sys


def readline():
    return sys.stdin.readline().rstrip()


N, M = map(int, readline().split(" "))
nCk = [[0 for i in range(j + 1)] for j in range(N + 1)]

for i in range(1, N + 1):
    nCk[i][0] = nCk[i][i] = 1


for i in range(2, N + 1):
    for j in range(1, i):
        nCk[i][j] = nCk[i - 1][j - 1] + nCk[i - 1][j]


print(nCk[N][M])
