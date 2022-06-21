import sys

sq2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512,
       1024, 2048, 4096, 8192, 16384, 32768]


def readline():
    return sys.stdin.readline().rstrip()


def getIndex(N, r, c):
    if(N == 1):
        return 2 * r + c

    sq_idx = 0
    half = sq2[N] // 2
    if(r >= half):
        sq_idx += 2
        r -= half
    if(c >= half):
        sq_idx += 1
        c -= half
    return half * half * sq_idx + getIndex(N-1, r, c)


N, r, c = map(int, readline().split(" "))
print(getIndex(N, r, c))
