import sys
from collections import deque


def readline():
    return sys.stdin.readline().rstrip()


N, M = map(int, readline().split())

miro = []

for i in range(N):
    miro.append(list(map(int, readline())))


def bfs():
    queue = deque([(0, 0)])
    count = miro[0][0] = 1
    while queue:
        (v_n, v_m) = queue.popleft()  # n, m, 이동해온 칸수
        count = miro[v_n][v_m]

        # 목적지 도달시 끝
        if v_n == N - 1 and v_m == M - 1:
            return count
        du = v_n - 1
        dd = v_n + 1
        dl = v_m - 1
        dr = v_m + 1
        if dd < N and miro[dd][v_m] == 1:
            queue.append((dd, v_m))
            miro[dd][v_m] = count + 1
        if du >= 0 and miro[du][v_m] == 1:
            queue.append((du, v_m))
            miro[du][v_m] = count + 1
        if dr < M and miro[v_n][dr] == 1:
            queue.append((v_n, dr))
            miro[v_n][dr] = count + 1
        if dl >= 0 and miro[v_n][dl] == 1:
            queue.append((v_n, dl))
            miro[v_n][dl] = count + 1
    return count


print(bfs())
