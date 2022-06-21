import sys
from collections import deque


def readline():
    return sys.stdin.readline().rstrip()


N, M = map(int, readline().split(" "))
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, readline().split(" "))
    graph[A].append(B)
    graph[B].append(A)

min_bacons = 25000000
min_friend = 0


# bfs
for i in range(1, N+1):
    bacons = 0  # 결과값
    visited = [False] * (N + 1)
    visited[i] = True
    queue = deque([[i, 0]])  # [friend, dist]
    while queue:
        [friend, dist] = queue.popleft()
        bacons += dist
        for n_v in graph[friend]:
            if visited[n_v] is False:
                visited[n_v] = True
                queue.append([n_v, dist + 1])
    if min_bacons > bacons:
        min_friend = i
        min_bacons = bacons
    elif min_bacons == bacons:
        if min_friend == 0:
            min_friend = i
        else:
            min_friend = min(min_friend, i)

print(min_friend)
