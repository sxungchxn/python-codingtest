import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())
graph = []
for _ in range(N):
    graph_item = list(map(int, readline().split(" ")))
    graph.append(graph_item)

result = [[0 for col in range(N)] for row in range(N)]


for start in range(N):
    stack = [start]
    while stack:
        v = stack[-1]
        all_visited = True
        for n_v in range(N):
            if graph[v][n_v] == 1 and result[start][n_v] == 0:
                result[start][n_v] = 1
                stack.append(n_v)
                all_visited = False
                break
        if all_visited:
            stack.pop()

for i in range(N):
    for j in range(N):
        print(result[i][j], end=' ')
    print()
