import sys
import heapq


def readline():
    return sys.stdin.readline().rstrip()


INF = int(1e9)

N, M, C = map(int, readline().split())

distance = [INF] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    X, Y, Z = map(int, readline().split())
    graph[X].append((Y, Z))  # X에서 Y까지는 Z의 거리가 걸린다.

# 다시 짜보기


def dijkstra(start):
    # 시작 노드 초기화 + 힙 초기화
    q = []
    heapq.heappush(q, (0, start))  # (시작 노드에서 해당 노드까지의 거리, 노드번호)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:  # 방문 중복 방지(최소값일 때만 방문)
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))


dijkstra(C)

total = 0
max_time = 0
for i in range(1, N+1):
    if i != C and distance[i] != INF:
        total += 1
        max_time = max(max_time, distance[i])

print(total, max_time)
