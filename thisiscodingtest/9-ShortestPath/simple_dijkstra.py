import sys


def readline():
    return sys.stdin.readline().rstrip()


INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]

# 각 노드별 방문 여부 테이블
visited = [False] * (n + 1)

# 출발지점에서 각 노드까지의 최단거리 테이블
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a->b 가는 거리 비용은 c임을 의미


# 방문 하지 않은 노드 중에서, 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True

    # 시작 노드에 인접한 노드들에 대해서 거리값을 갱신
    for j in graph[start]:
        # j[0] : start에 인접한 노드, j[1] : start에서 해당 노드까지의 거리
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해서 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
