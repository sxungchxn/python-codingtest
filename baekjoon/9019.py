import sys
from collections import deque


# operation 개선하기, visited 저장방식 개선하기

def readline():
    return sys.stdin.readline().rstrip()


def left(num):
    left_side = (num % 1000) * 10
    right_side = num // 1000
    return left_side + right_side


def right(num):
    last = num % 10
    left_side = num // 10
    return 1000*last + left_side


def double(src):
    return (src * 2) % 10000


def substract(src):
    return src - 1 if src - 1 >= 0 else 9999


def findTarget(src, dst):
    visited = [False] * 10001
    queue = deque()
    queue.append([src, ""])
    while queue:
        now, op = queue.popleft()
        if now == dst:
            return op
        result = double(now)
        if visited[result] is False:
            visited[result] = True
            queue.append([result, op + "D"])
        result = substract(now)
        if visited[result] is False:
            visited[result] = True
            queue.append([result, op + "S"])
        result = left(now)
        if visited[result] is False:
            visited[result] = True
            queue.append([result, op + "L"])
        result = right(now)
        if visited[result] is False:
            visited[result] = True
            queue.append([result, op + "R"])


T = int(readline())

for _ in range(T):
    A, B = map(int, readline().split(" "))
    print(findTarget(A, B))
