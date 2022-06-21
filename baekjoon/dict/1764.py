import sys


def readline():
    return sys.stdin.readline().rstrip()


listen = dict()
result = dict()

N, M = map(int, readline().split(" "))

for _ in range(N):
    name = readline()
    listen[name] = 1

for _ in range(M):
    name = readline()
    if name in listen:
        result[name] = 1

print(len(result))

for key in sorted(list(result.keys())):
    print(key)
