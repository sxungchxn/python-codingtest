import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())
graph = [[] for _ in range(N + 1)]
parents = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, readline().split(" "))
    graph[a].append(b)
    graph[b].append(a)


def dfs():
    global graph, parents
    stk = [1]
    while stk:
        parent = stk[-1]
        all_visited = True
        for child in graph[parent]:
            if parents[child] == 0:
                stk.append(child)
                parents[child] = parent
                all_visited = False
                break
        if all_visited:
            stk.pop()


dfs()

for i in range(2, N+1):
    print(parents[i])
