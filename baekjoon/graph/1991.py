import sys


def readline():
    return sys.stdin.readline().rstrip()


def index(ch):
    return ord(ch) - ord('A')


N = int(readline())
graph = [[] for i in range(N)]
visited = [False] * N


def dfs1(alpha):
    global visited
    print(alpha, end='')
    idx = index(alpha)
    visited[idx] = True
    for child in graph[idx]:
        child_idx = index(child)
        if child != '.' and visited[child_idx] == False:
            dfs1(child)


def dfs2(alpha):
    global visited
    idx = index(alpha)
    visited[idx] = True
    left_alpha = graph[idx][0]
    right_alpha = graph[idx][1]

    if left_alpha != '.':
        child_idx = index(left_alpha)
        if visited[child_idx] == False:
            visited[child_idx] = True
            dfs2(left_alpha)
    print(alpha, end='')
    if right_alpha != '.':
        child_idx = index(right_alpha)
        if visited[child_idx] == False:
            visited[child_idx] = True
            dfs2(right_alpha)


def dfs3(alpha):
    global visited
    idx = index(alpha)
    visited[idx] = True
    left_alpha = graph[idx][0]
    right_alpha = graph[idx][1]

    if left_alpha != '.':
        child_idx = index(left_alpha)
        if visited[child_idx] == False:
            visited[child_idx] = True
            dfs3(left_alpha)
    if right_alpha != '.':
        child_idx = index(right_alpha)
        if visited[child_idx] == False:
            visited[child_idx] = True
            dfs3(right_alpha)
    print(alpha, end='')


for _ in range(N):
    line = readline().split(" ")
    graph[index(line[0])] = line[1:]


dfs1('A')
print()

visited = [False] * N
dfs2('A')
print()

visited = [False] * N
dfs3('A')
print()
