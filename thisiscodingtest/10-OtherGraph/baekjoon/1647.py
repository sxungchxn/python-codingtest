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


N, M = map(int, readline().split())

parent = [0] * (N+1)  # 1 ~ N

for i in range(1, N+1):
    parent[i] = i

# edge 추가
edges = []
for _ in range(M):
    A, B, C = map(int, readline().split())  # A - B의 비용 = C
    edges.append((C, A, B))  # 비용, A, B

edges.sort()

costs = []  # 유지비들의 집합

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        costs.append(cost)

costs.sort()
cost_length = len(costs)
result = 0
for i in range(cost_length - 1):
    result += costs[i]

print(result)
