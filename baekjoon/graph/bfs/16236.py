import sys
from collections import deque


def readline():
    return sys.stdin.readline().rstrip()


graph = []
N = int(readline())
INIT_DIST = 99999999
visited = [[False for i in range(N)] for j in range(N)]
baby_size = 2  # 현재 아기상어 크기
baby_cnt = 0  # 아기상어가 먹은 물고기 개수
baby_r = 0
baby_c = 0

for r in range(N):
    line = list(map(int, readline().split(" ")))
    for c in range(N):
        if line[c] == 9:
            baby_r = r
            baby_c = c
    graph.append(line)


def bfs(start_r, start_c, fish_size):
    global N, baby_cnt, visited, INIT_DIST
    queue = deque([[start_r, start_c, 0]])
    visited = [[False for i in range(N)] for j in range(N)]
    visited[start_r][start_c] = True
    min_r = -1
    min_c = -1
    min_dist = INIT_DIST
    while queue:
        r, c, cnt = queue.popleft()
        if graph[r][c] >= 1 and graph[r][c] <= 6 and graph[r][c] < fish_size:
            if min_dist > cnt:
                min_r = r
                min_c = c
                min_dist = cnt
            elif min_dist == cnt:
                if min_r > r:
                    min_r = r
                    min_c = c
                elif min_r == r and min_c > c:
                    min_c = c
            elif min_dist != INIT_DIST and cnt > min_dist:
                continue
        r_d = r + 1
        r_u = r - 1
        c_l = c - 1
        c_r = c + 1
        if r_d < N and visitable(r_d, c, fish_size):
            visited[r_d][c] = True
            queue.append([r_d, c, cnt + 1])
        if r_u >= 0 and visitable(r_u, c, fish_size):
            visited[r_u][c] = True
            queue.append([r_u, c, cnt + 1])
        if c_l >= 0 and visitable(r, c_l, fish_size):
            visited[r][c_l] = True
            queue.append([r, c_l, cnt + 1])
        if c_r < N and visitable(r, c_r, fish_size):
            visited[r][c_r] = True
            queue.append([r, c_r, cnt + 1])
    return [min_r, min_c, min_dist]


def visitable(r, c, from_size):
    global visited, graph
    if visited[r][c] == False and graph[r][c] <= from_size:
        return True
    else:
        return False


result = 0
bfs_result = bfs(baby_r, baby_c, baby_size)
while bfs_result[0] != -1:
    baby_cnt += 1
    if baby_cnt >= baby_size:
        baby_size += 1
        baby_cnt = 0

    graph[baby_r][baby_c] = 0
    baby_r = bfs_result[0]
    baby_c = bfs_result[1]
    result += bfs_result[2]
    graph[baby_r][baby_c] = 0

    bfs_result = bfs(baby_r, baby_c, baby_size)

print(result)
