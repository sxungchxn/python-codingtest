import sys


def readline():
    return sys.stdin.readline().rstrip()


N, M = map(int, readline().split())
table = []

for i in range(N):
    table.append(list(map(int, readline().split())))

sums = [[0]*N for i in range(N)]
sums[0][0] = table[0][0]

for i in range(1, N):
    sums[i][0] = sums[i-1][0] + table[i][0]
    sums[0][i] = sums[0][i-1] + table[0][i]

for i in range(1, N):
    for j in range(1, N):
        sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + table[i][j]


for i in range(M):
    x1, y1, x2, y2 = map(int, readline().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    res = sums[x2][y2]
    if y1 - 1 >= 0:
        res -= sums[x2][y1 - 1]
    if x1 - 1 >= 0:
        res -= sums[x1 - 1][y2]
    if x1 - 1 >= 0 and y1 - 1 >= 0:
        res += sums[x1 - 1][y1 - 1]
    print(res)
