import sys
from collections import deque


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())

queue = deque()


def isEmpty(queue):
    return len(queue) == 0


for _ in range(N):
    line = readline().split(" ")
    if len(line) == 2:
        queue.append(int(line[1]))
    else:
        cmd = line[0]
        if cmd == "pop":
            if isEmpty(queue):
                print(-1)
            else:
                print(queue.popleft())
        elif cmd == "size":
            print(len(queue))
        elif cmd == "empty":
            print(int(isEmpty(queue)))
        elif cmd == "front":
            if isEmpty(queue):
                print(-1)
            else:
                print(queue[0])
        elif cmd == "back":
            if isEmpty(queue):
                print(-1)
            else:
                print(queue[-1])
