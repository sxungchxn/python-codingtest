# Union Find 알고리즘을 활용하여
# 주어진 그래프의 사이클 유무를 확인할 수 있다.


import sys


def readline():
    return sys.stdin.readline().rstrip()


# 특정 원소가 소간 집합을 찾기 = 루트 부모 찾기
def find_parent(parent, x):
    # 루트 노드 = 부모노드가 자기 자신인 노드
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  # 경로 압축 기법 적용
    return parent[x]


# 두 원소가 속한 집합을 합치기
# 부모가 더 큰 요소의 부모를 부모가 더 작은 요소의 부모로 설정
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, readline().split())
parent = [0] * (v + 1)

for i in range(1, v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, readline().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)
