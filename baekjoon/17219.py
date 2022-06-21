import sys


def readline():
    return sys.stdin.readline().rstrip()


N, M = map(int, readline().split(" "))

passwords = {}

for _ in range(N):
    address, psw = readline().split(" ")
    passwords[address] = psw

for _ in range(M):
    address = readline()
    print(passwords[address])
