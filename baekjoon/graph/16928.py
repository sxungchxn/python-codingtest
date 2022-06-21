import sys
from collections import deque


def readline():
    return sys.stdin.readline().rstrip()


ladders = {}
snakes = {}
N, M = map(int, readline().split(" "))
for i in range(N + M):
    x, y = map(int, readline().split(" "))
    if i < N:
        ladders[x] = y
    else:
        snakes[x] = y

queue = deque([[1, 0]])  # num, count
visited = [[-1, -1] for _ in range(102)]  # last num, count at last visit
result = -1


def visitable(num, to, count):
    global visited
    if visited[to][0] == -1:
        return True
    elif visited[to][1] > count:
        return True
    elif visited[to][1] == count and visited[to][0] != num:
        return True
    else:
        return False


while queue:
    num, count = queue.popleft()
    if num == 100:
        if result == -1:
            result = count
        else:
            result = min(result, count)
        continue
    if num in ladders:
        target = ladders[num]
        if visitable(num, target, count):
            visited[target] = [num, count]
            queue.append([target, count])
    elif num in snakes:
        target = snakes[num]
        if visitable(num, target, count):
            visited[target] = [num, count]
            queue.append([target, count])
    else:
        for i in range(1, 7):
            target = num + i
            if target <= 100 and visitable(num, target, count + 1):
                visited[target] = [num, count + 1]
                queue.append([target, count + 1])

print(result)
