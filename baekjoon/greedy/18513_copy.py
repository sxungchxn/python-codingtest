import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

waters = list(map(int, input().split()))
queue = deque()

pos_set = set()

for water in waters:
    pos_set.add(water)
    queue.append((water - 1, 1))
    queue.append((water + 1, 1))


count = 0
result = 0

while count < K:
    pos, val = queue.popleft()
    if pos not in pos_set:
        pos_set.add(pos)
        count += 1
        result += val
        queue.append((pos + 1, val + 1))
        queue.append((pos - 1, val + 1))

print(result)
