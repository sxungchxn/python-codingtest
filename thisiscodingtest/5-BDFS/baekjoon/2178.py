import sys
from collections import deque


def readline():
    return sys.stdin.readline().rstrip()


N, M = map(int, readline().split())

miro = []

for i in range(N):
    row_list = []
    line = readline()
    for num_char in line:
        row_list.append(int(num_char))
    miro.append(row_list)


def bfs(start_n, start_m):
    queue = deque([(start_n, start_m)])
    miro[start_n][start_m] = 1

    while queue:
        st_n, st_m = queue.popleft()

        if(st_n == N-1 and st_m == M-1):
            break
        du = st_n + 1
        dd = st_n - 1
        dl = st_m - 1
        dr = st_m + 1
        dist = miro[st_n][st_m]
        if du < N and miro[du][st_m] == 1:
            miro[du][st_m] = dist + 1
            queue.append((du, st_m))
        if dd >= 0 and miro[dd][st_m] == 1:
            miro[dd][st_m] = dist + 1
            queue.append((dd, st_m))
        if dl >= 0 and miro[st_n][dl] == 1:
            miro[st_n][dl] = dist + 1
            queue.append((st_n, dl))
        if dr < M and miro[st_n][dr] == 1:
            miro[st_n][dr] = dist + 1
            queue.append((st_n, dr))
    return miro[N-1][M-1]


print(bfs(0, 0), end='')
