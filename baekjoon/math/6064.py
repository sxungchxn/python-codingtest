import sys


def readline():
    return sys.stdin.readline().rstrip()


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def lcm(a, b):
    return int(a * b / gcd(a, b))


T = int(readline())


for _ in range(T):
    M, N, x, y = map(int, readline().split(" "))
    cnt = x
    tempY = x  # x번째 숫자부터 시작 => y를 x와 맞춘뒤 M의 주기만큼 증가
    for i in range(N):
        if tempY % N == 0:
            ty = N
        else:
            ty = tempY % N
        if ty == y:
            break
        tempY = ty + M
        cnt += M
    if cnt > lcm(M, N):
        print(-1)
    else:
        print(cnt)
