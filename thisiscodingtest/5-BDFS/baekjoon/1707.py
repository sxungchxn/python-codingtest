import sys
from collections import deque


def readline():
    return sys.stdin.readline().rstrip()


K = int(readline())
graph = []
marked = []
visited = []
result = True


def bfs(start):
    queue = deque([start])
    marked[start] = 1
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if marked[neighbor] == 0:
                marked[neighbor] = marked[node] * -1
                queue.append(neighbor)


def check_bfs(start):
    global result
    queue = deque([start])
    stop = False
    while queue:
        node = queue.popleft()
        visited[node] = 1
        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                if marked[neighbor] != marked[node]:
                    queue.append(neighbor)
                else:
                    stop = True
        if stop:
            result = False
            break


def check_all_marked(marked, V, start):
    for i in range(start, V+1):
        if marked[i] == 0:
            return i
    return -1


for k in range(K):
    V, E = map(int, readline().split())
    graph = [[] for _ in range(V+1)]
    marked = [0] * (V+1)
    for i in range(E):
        u, v = map(int, readline().split())
        graph[u].append(v)
        graph[v].append(u)
    all_marked = check_all_marked(marked, V, 1)
    while all_marked != -1:
        bfs(all_marked)
        all_marked = check_all_marked(marked, V, all_marked)
    visited = [0] * (V+1)
    result = True
    all_marked = check_all_marked(visited, V, 1)
    while all_marked != -1:
        check_bfs(all_marked)
        if result == False:
            break
        all_marked = check_all_marked(visited, V, all_marked)
    if result:
        print("YES")
    else:
        print("NO")
