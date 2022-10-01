import sys


def readline():
    return sys.stdin.readline().rstrip()


INF = int(1e12)

n = int(readline())
m = int(readline())

graph = [[INF] * (n+1) for _ in range(n + 1)]


for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, readline().split(" "))
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] != INF:
            print(graph[a][b], end=' ')
        else:
            print(0, end=' ')
    print()
