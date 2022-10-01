import sys


def readline():
    return sys.stdin.readline().rstrip()


n = int(readline())
graph = [[] for _ in range(n + 1)]  # 길이 있는지 여부만 표시
dist = {}

for _ in range(n - 1):
    a, b, c = map(int, readline().split(" "))
    graph[a].append(b)
    graph[b].append(a)
    dist[(a, b)] = dist[(b, a)] = c

max_dist = 0
max_node = 1

for i in range(2):
    if i == 0:
        start = 1
    else:
        max_dist = 0
        start = max_node
    stack = [(start, 0)]
    visited = [False] * (n + 1)
    visited[start] = True
    while stack:
        node, dis = stack[-1]
        all_visited = True
        for c in graph[node]:
            if visited[c] == False:
                visited[c] = True
                new_dist = dis + dist[(node, c)]
                stack.append((c, new_dist))
                if max_dist < new_dist:
                    max_dist = new_dist
                    max_node = c
                all_visited = False
                break
        if all_visited:
            stack.pop()

print(max_dist)
