import sys
from collections import deque


def readline():
    return sys.stdin.readline().rstrip()


M, N = map(int, readline().split())
tomatos = []  # 전체 토마토 맵(1이면 익은토마토, 0은 신선토마토, -1은 빈 토마토)
starts = []  # 익은 토마토 시작점들의 집합
freshes = 0  # 입력으로 주어진 신선 토마토 개수
result = 0

for i in range(N):
    line = list(map(int, readline().split()))
    for j in range(M):
        if line[j] == 0:
            freshes += 1
        if line[j] == 1:
            starts.append((i, j))
    tomatos.append(line)

queue = deque(starts)

while queue:
    n, m = queue.popleft()
    if tomatos[n][m] > 0:
        result = max(result, tomatos[n][m])
        du = n + 1
        dd = n - 1
        dl = m - 1
        dr = m + 1
        new_tomato = tomatos[n][m] + 1
        if du < N and tomatos[du][m] == 0:
            tomatos[du][m] = new_tomato
            freshes -= 1
            queue.append((du, m))
        if dd >= 0 and tomatos[dd][m] == 0:
            tomatos[dd][m] = new_tomato
            freshes -= 1
            queue.append((dd, m))
        if dr < M and tomatos[n][dr] == 0:
            tomatos[n][dr] = new_tomato
            freshes -= 1
            queue.append((n, dr))
        if dl >= 0 and tomatos[n][dl] == 0:
            tomatos[n][dl] = new_tomato
            freshes -= 1
            queue.append((n, dl))

if freshes > 0:
    result = -1
else:
    result -= 1

print(result, end='\n')
