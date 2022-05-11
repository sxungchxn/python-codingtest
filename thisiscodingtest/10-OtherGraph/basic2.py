import sys


def readline():
    return sys.stdin.readline().rstrip()


# 주어진 요소 x의 부모 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, readline().split())
parent = [0] * (N + 1)  # 0 ~ N + 1

for i in range(0, N + 1):
    parent[i] = i


for _ in range(M):
    op, a, b = map(int, readline().split())
    if op == 0:
        union_parent(parent, a, b)
    else:
        if(find_parent(parent, a) == find_parent(parent, b)):
            print("YES")
        else:
            print("NO")
