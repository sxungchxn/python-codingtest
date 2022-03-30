import sys
from collections import deque


def readline():
    return sys.stdin.readline().rstrip()


N, M, V = map(int, readline().split())

vertex = [[] for _ in range(N+1)]  # 1 ~ N까지 인접노드 표시
visited = [False] * (N+1)  # 1 ~ N까지 방문여부 표시


for i in range(M):
    start, end = map(int, readline().split())
    vertex[start].append(end)
    vertex[end].append(start)

for i in range(N+1):
    vertex[i].sort()


def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for ver in vertex[v]:
        if visited[ver] == False:
            dfs(ver)


def bfs(start):
    queue = deque([start])
    while queue:
        target = queue.popleft()
        if visited[target] == False:
            visited[target] = True
            for ver in vertex[target]:
                if visited[ver] == False:
                    queue.append(ver)
            print(target, end=' ')


dfs(V)
print('')
visited = [False] * (N+1)  # 1 ~ N까지 방문여부 표시
bfs(V)
