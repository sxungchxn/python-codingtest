import sys

INF = int(1e9)


def readline():
    return sys.stdin.readline().rstrip()


def passable(a, b):
    if a != INF or b != INF:
        return 1
    else:
        return


N = int(readline())

graph = []
for _ in range(N):
    graph_item = list(map(int, readline().split(" ")))
    for i in range(N):
        if graph_item[i] == 0:
            graph_item[i] = INF
    graph.append(graph_item)

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(N):
    for j in range(N):
        if graph[i][j] != INF:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
