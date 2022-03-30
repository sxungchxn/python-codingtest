import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000000)

N, M = map(int, input().split())

dducks = list(map(int, input().split()))

print(N, M, dducks)
