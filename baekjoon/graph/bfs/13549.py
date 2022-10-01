import sys
import heapq


def readline():
    return sys.stdin.readline().rstrip()


N, K = map(int, readline().split())


visited = [200000] * 200001
visited[N] = 0

min_time = -1

# queue = deque([N])


class Data:
    def __init__(self, pos, time):
        self.pos = pos
        self.time = time

    def __lt__(self, other):
        return self.time < other.time

    def __le__(self, other):
        return self.time <= other.time

    def __eq__(self, other):
        return self.time == other.time


minHeap = []
heapq.heappush(minHeap, Data(N, 0))

while minHeap:
    inst = heapq.heappop(minHeap)
    pos = inst.pos
    time = inst.time

    if pos == K:
        if min_time == -1:
            min_time = time
        elif min_time > time:
            min_time = time
    if pos < K and visited[pos * 2] > time:
        visited[pos * 2] = time
        heapq.heappush(minHeap, Data(pos * 2, time))
    if pos < K and visited[pos + 1] > time + 1:
        visited[pos + 1] = time + 1
        heapq.heappush(minHeap, Data(pos + 1, time + 1))
    if pos > 0 and visited[pos - 1] > time + 1:
        visited[pos - 1] = time + 1
        heapq.heappush(minHeap, Data(pos - 1, time + 1))

print(min_time)
