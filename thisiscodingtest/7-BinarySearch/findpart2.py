import sys


def readline():
    return sys.stdin.readline().rstrip()


# 부품의 개수
N = int(readline())
# 입력값을 집합에 넣기
parts = set(map(int, readline().split()))

M = int(readline())
targets = list(map(int, readline().split()))

for target in targets:
    if target in parts:
        print('yes', end=' ')
    else:
        print('no', end=' ')
