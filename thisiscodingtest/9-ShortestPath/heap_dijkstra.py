# 특정 노드에서 다른 노드로의 최소거리를 알려주는 알고리즘 + 힙사용
# 시간복잡도 : O(E * log(V))

import sys
import heapq


def readline():
    return sys.stdin.readline().rstrip()


INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]

# 출발지점에서 각 노드까지의 최단거리 테이블
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a->b 가는 거리 비용은 c임을 의미


def dijkstra(start):
    q = []
    # 시작노드로 가기 위한 최단 경로는 0으로 설정 후 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # q가 비어있지 않을때까지
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
