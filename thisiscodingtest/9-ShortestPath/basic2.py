import sys


def readline():
    return sys.stdin.readline().rstrip()


INF = int(1e9)

N, M = map(int, readline().split())

graph = [[INF] * (N+1) for _ in range(N+1)]

for a in range(N + 1):
    for b in range(N+1):
        if a == b:
            graph[a][b] = 0

for _ in range(M):
    a, b = map(int, readline().split())
    graph[a][b] = graph[b][a] = 1

X, K = map(int, readline().split())

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

dist = graph[1][K] + graph[K][X]
if dist >= INF:
    print(-1)
else:
    print(dist)
