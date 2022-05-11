import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())
parts = list(map(int, readline().split()))

M = int(readline())
targets = list(map(int, readline().split()))

parts.sort()
for target in targets:
    start = 0
    end = N - 1
    found = False
    while(start <= end):
        mid = (start + end) // 2
        if parts[mid] == target:
            found = True
            break
        elif parts[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    if found:
        print("yes", end=" ")
    else:
        print("no", end=" ")
