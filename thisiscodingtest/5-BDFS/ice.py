import sys


def readline():
    return sys.stdin.readline().rstrip()


result = 0

N, M = map(int, readline().split())

ice = [[] for _ in range(N)]

for i in range(N):
    ice[i] = list(map(int, readline()))

# 불필요한 함수


def get_nears(pos_x, pos_y):
    nears = []
    if pos_x + 1 < M == 0:
        nears.append((pos_x+1, pos_y))
    if pos_x - 1 >= 0 == 0:
        nears.append((pos_x - 1, pos_y))
    if pos_y + 1 < N == 0:
        nears.append((pos_x, pos_y + 1))
    if pos_y - 1 >= 0 == 0:
        nears.append((pos_x, pos_y - 1))
    return nears


# 아래와 같이 재귀를 구성할 경우 ice가 딸려 가기 때문에
# 굉장히 무거운 재귀 작업이 이뤄질 수 있다.
def dfs(ice, start):
    start_x, start_y = start
    if ice[start_y][start_x] == 0:
        ice[start_y][start_x] = 2
        nears = get_nears(start_x, start_y, ice)
        for near in nears:
            near_x, near_y = near
            if ice[near_y][near_x] == 0:
                dfs(ice, near)


for i in range(N):
    for j in range(M):
        if ice[i][j] == 0:
            dfs(ice, (j, i))
            result += 1

print(result)
