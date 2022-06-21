import sys
from collections import deque


def readline():
    return sys.stdin.readline().rstrip()


color_map = []
N = int(readline())


for _ in range(N):
    color_line = list(readline())
    color_map.append(color_line)


def rule1(a, b):
    if a == b:
        return True
    else:
        return False


def rule2(a, b):
    if a == 'B':
        if a == b:
            return True
        else:
            return False
    else:
        if b == 'B':
            return False
        else:
            return True


def bfs(N, rule):
    global color_map
    queue = deque([])
    visited = [[False for i in range(N)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                # print('false at ', i, j)
                count += 1
                visited[i][j] = True
                queue.append([i, j])
                while queue:
                    r, c = queue.popleft()
                    old_color = color_map[r][c]
                    r_u = r - 1
                    r_d = r + 1
                    c_l = c - 1
                    c_r = c + 1
                    if r_u >= 0 and visited[r_u][c] == False:
                        new_color = color_map[r_u][c]
                        if rule(old_color, new_color):
                            visited[r_u][c] = True
                            queue.append([r_u, c])
                    if r_d < N and visited[r_d][c] == False:
                        new_color = color_map[r_d][c]
                        if rule(old_color, new_color):
                            visited[r_d][c] = True
                            queue.append([r_d, c])
                    if c_l >= 0 and visited[r][c_l] == False:
                        new_color = color_map[r][c_l]
                        if rule(old_color, new_color):
                            visited[r][c_l] = True
                            queue.append([r, c_l])
                    if c_r < N and visited[r][c_r] == False:
                        new_color = color_map[r][c_r]
                        if rule(old_color, new_color):
                            visited[r][c_r] = True
                            queue.append([r, c_r])
    return count


# bfs 1 => R != G != B
# bfs 2 => R == G != B
print(bfs(N, rule1), bfs(N, rule2))
