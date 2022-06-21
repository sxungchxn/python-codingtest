import sys


def readline():
    return sys.stdin.readline().rstrip()


M = int(readline())
N = 0

for _ in range(M):
    words = readline().split(" ")
    if len(words) == 1:
        op = words[0]
        if op == "all":
            N = (1 << 21) - 1
        elif op == "empty":
            N = 0
    else:
        [op, x] = words
        x = int(x)
        if op == "add":
            N |= (1 << x)
        elif op == "remove":
            N &= ~(1 << x)
        elif op == "check":
            print(1 if N & (1 << x) > 0 else 0)
        elif "toggle":
            N ^= (1 << x)
