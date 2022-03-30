import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())

count = [0] * 10001

for i in range(N):
    num = int(readline())
    count[num] += 1

for i in range(1, 10001):
    for j in range(count[i]):
        print(i, end='\n')
