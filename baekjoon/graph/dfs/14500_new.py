import sys


def readline():
    return sys.stdin.readline().rstrip()


N, M = map(int, readline().split(" "))

graph = []

for _ in range(N):
    line = list(map(int, readline().split(" ")))
    graph.append(line)

max_sum = 0

# dfs


def dfs(st_r, st_c):
    global N, M, max_sum
    visited = [[False for i in range(M)] for j in range(N)]
    stack = [[st_r, st_c, 1, graph[st_r][st_c]]]
    visited[st_r][st_c] = True
    while stack:
        r, c, level, sum = stack[-1]
        if level == 4:
            max_sum = max(max_sum, sum)
            stack.pop()
            continue
        r_d = r + 1
        r_u = r - 1
        c_l = c - 1
        c_r = c + 1
        d_visit = r_d < N and (visited[r_d][c] == False)
        u_visit = r_u >= 0 and level > 1 and (visited[r_u][c] == False)
        l_visit = c_l >= 0 and level > 1 and (visited[r][c_l] == False)
        r_visit = c_r < M and (visited[r][c_r] == False)
        if level == 2:
            # ㅗ패턴 체크
            if u_visit and d_visit:
                max_sum = max(max_sum, sum + graph[r_u][c] + graph[r_d][c])
            if u_visit and r_visit:
                max_sum = max(max_sum, sum + graph[r_u][c] + graph[r][c_r])
            if r_visit and d_visit:
                max_sum = max(max_sum, sum + graph[r][c_r] + graph[r_d][c])
            if l_visit and d_visit:
                max_sum = max(max_sum, sum + graph[r][c_l] + graph[r_d][c])
            if l_visit and r_visit:
                max_sum = max(max_sum, sum + graph[r][c_l] + graph[r][c_r])
        if d_visit:
            visited[r_d][c] = True
            stack.append([r_d, c, level + 1, sum + graph[r_d][c]])
            continue
        if u_visit:
            visited[r_u][c] = True
            stack.append([r_u, c, level + 1, sum + graph[r_u][c]])
            continue
        if l_visit:
            visited[r][c_l] = True
            stack.append([r, c_l, level + 1, sum + graph[r][c_l]])
            continue
        if r_visit:
            visited[r][c_r] = True
            stack.append([r, c_r, level + 1, sum + graph[r][c_r]])
            continue
        stack.pop()


for i in range(N):
    for j in range(M):
        dfs(i, j)

print(max_sum)
