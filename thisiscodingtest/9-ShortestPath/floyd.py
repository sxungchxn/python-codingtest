# 모든 노드에서 노드로의 거리를 파악하는데 사용되는 알고리즘
# 시간복잡도 : O(N^3)


import sys


def readline():
    return sys.stdin.readline().rstrip()


INF = int(1e9)

n = int(readline())
m = int(readline())

# 그래프 생성, 무한으로 초기화
# 특정 노드에서 다른 노드로 이동하는 최단 거리 기록
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자신에게 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0


# 각 간선에 대한 정보를 입력 받고 그것을 테이블에 반영
for _ in range(m):
    a, b, c = map(int, readline().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] == INF:
                print("INF", end=" ")
            else:
                print(graph[a][b], end=" ")
    print()
