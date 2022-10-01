import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())

paths = readline().split(" ")

pos = [1, 1]

for path in paths:
    if path == "L" and pos[1] - 1 >= 1:
        pos[1] -= 1
    elif path == "R" and pos[1] + 1 <= N:
        pos[1] += 1
    elif path == "U" and pos[0] - 1 >= 1:
        pos[0] -= 1
    elif path == "D" and pos[0] + 1 <= N:
        pos[0] += 1

print(pos[0], pos[1])
