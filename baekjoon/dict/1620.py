import sys


def readline():
    return sys.stdin.readline().rstrip()


pks = []
N, M = map(int, readline().split(" "))

for _ in range(N):
    name = readline()
    pks.append(name)

pks_dict = dict()

for i in range(len(pks)):
    pks_dict[pks[i]] = i

for _ in range(M):
    cmd = readline()
    if ord(cmd[0]) >= 48 and ord(cmd[0]) <= 57:
        cmd = int(cmd)
        print(pks[cmd - 1])
    else:
        print(pks_dict[cmd] + 1)
