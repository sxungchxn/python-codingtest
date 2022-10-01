import sys
import heapq


def readline():
    return sys.stdin.readline().rstrip()


N, K = map(int, readline().split())


visited = [200000] * 200001
visited[N] = 0

min_time = -1

# queue = deque([N])

# 객체 연산자 정의
# https://lovedh.tistory.com/entry/Python-Priority-Queue%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90-%EA%B0%9D%EC%B2%B4-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0


class Data:
    def __init__(self, pos, time):
        self.pos = pos
        self.time = time

    # less than
    def __lt__(self, other):
        return self.time < other.time

    # less or equal
    def __le__(self, other):
        return self.time <= other.time

    # equal
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
