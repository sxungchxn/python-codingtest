# 위상 정렬
# 사이클이 없는 방향성 그래프(DAG : Directed Acycic Graph)에서 방향성을 해치지 않으면서 모든 노드를 방문


import sys
from collections import deque


def readline():
    return sys.stdin.readline().rstrip()


v, e = map(int, readline().split())

indegree = [0] * (v + 1)

graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, readline().split())
    graph[a].append(b)

    indegree[b] += 1  # 진입 차수 증가(b에 대해서)


def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:  # 진입 차수가 0인 노드 찾아서 큐에 넣기
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)  # 방문 순서 표시

        # 인접한 노드들로 이어지는 간선 제거 => 이웃한 노드들의 진입 차수 감소
        for i in graph[now]:
            indegree[i] -= 1
            if(indegree[i] == 0):
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()
