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

for i in range(e):
    a, b = map(int, readline().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블 : ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')
