import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())
M = int(readline())

neighbors = [[] for _ in range(N + 1)]

for i in range(M):
    start, end = map(int, readline().split())
    neighbors[start].append(end)
    neighbors[end].append(start)

visited = [False] * (N+1)


result = 0


def dfs(v, result):
    visited[v] = True
    if v != 1:
        result += 1
    for ver in neighbors[v]:
        if visited[ver] == False:
            result = dfs(ver, result)
    return result


result = dfs(1, result)
print(result)
