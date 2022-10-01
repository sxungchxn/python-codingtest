import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

poses = list(map(int, input().split()))

visited = set()
num_queue = deque()

# queue =>  <- |    | <-
count = 0
result = 0
for pos in poses:
    num_queue.append((pos, 1))
    visited.add(pos)

stop_flag = False

while num_queue:
    pos, score = num_queue.popleft()
    for d in [1, -1]:
        new_pos = pos + d
        if new_pos in visited:
            continue
        count += 1
        result += score
        visited.add(new_pos)
        num_queue.append((new_pos, score+1))
        if count == K:
            stop_flag = True
            break
    if stop_flag:
        break


print(result)
