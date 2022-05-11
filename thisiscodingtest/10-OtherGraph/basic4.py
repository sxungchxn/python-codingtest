import sys
from collections import deque


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())

indegree = [0] * (N + 1)
lecture = [0] * (N + 1)
graph = [[] for i in range(N+1)]

for i in range(1, N+1):
    input = list(map(int, readline().split()))
    input_len = len(input)
    lecture[i] = input[0]
    for j in range(1, input_len - 1):
        graph[input[j]].append(i)
        indegree[i] += 1


def topology_sort():
    result = [0] * (N+1)
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            result[i] = lecture[i]
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + lecture[i])
            print(f'add to {i} with {lecture[now]}')
            if(indegree[i] == 0):
                q.append(i)
    return result


times = topology_sort()
for i in range(1, N+1):
    print(times[i])
