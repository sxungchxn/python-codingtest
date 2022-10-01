import sys
import heapq


def readline():
    return sys.stdin.readline().rstrip()


INF = int(1e9)

V, E = map(int, readline().split(" "))
K = int(readline())

graph = [{} for _ in range(V + 1)]
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, readline().split(" "))

    if v not in graph[u]:
        graph[u][v] = w
    else:
        graph[u][v] = min(graph[u][v], w)


def dijkstra(start):
    global distance
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        keys = list(graph[now])
        for key in keys:
            cost = dist + graph[now][key]
            if cost < distance[key]:
                distance[key] = cost
                heapq.heappush(q, (cost, key))


dijkstra(K)

for i in range(1, V+1):
    if i == K:
        print(0)
    else:
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])
