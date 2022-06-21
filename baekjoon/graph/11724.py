import sys
from collections import deque

count = 0


def readline():
    return sys.stdin.readline().rstrip()


def bfs(graph, start, visited):
    global count
    count += 1
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for n_v in graph[v]:
            if visited[n_v] is False:
                visited[n_v] = True
                queue.append(n_v)


N, M = map(int, readline().split(" "))

visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, readline().split(" "))
    graph[u].append(v)
    graph[v].append(u)


for i in range(1, N+1):
    if visited[i] is False:
        bfs(graph, i, visited)

print(count)
