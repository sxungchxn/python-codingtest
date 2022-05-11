# Minimum Spanning Tree(최소 신장 트리)
# 그래프에서 모든 노드를 지나면서 사이클이 존재하지 않는 부분 그래프
# 트리의 조건 => 그래프 상의 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다.

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

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, readline().split())
    edges.append((cost, a, b))

edges.sort()  # cost를 기준으로 오름차순 정렬 진행

for edge in edges:
    cost, a, b = edge
    # cycle이 발생하지 않는 노드들 만 한정해 추가
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
