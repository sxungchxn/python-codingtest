import sys


def readline():
    return sys.stdin.readline().rstrip()


N, M = map(int, readline().split())

ice_map = []
result = 0

for i in range(N):
    ice_map.append(list(map(int, readline())))


def dfs(start_n, start_m):
    ice_map[start_n][start_m] = 2
    dr = start_m + 1
    dl = start_m - 1
    du = start_n - 1
    dd = start_n + 1
    if dd < N and ice_map[dd][start_m] == 0:
        dfs(dd, start_m)
    if du >= 0 and ice_map[du][start_m] == 0:
        dfs(du, start_m)
    if dr < M and ice_map[start_n][dr] == 0:
        dfs(start_n, dr)
    if dl >= 0 and ice_map[start_n][dl] == 0:
        dfs(start_n, dl)


for i in range(N):
    for j in range(M):
        if ice_map[i][j] == 0:
            dfs(i, j)
            result += 1

print(result)
