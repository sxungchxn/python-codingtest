import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000000)

N = int(input())

maps = []
for i in range(N):
    map_line = list(map(int, input().split()))
    maps.append(map_line)

result = 0


def find_ways(r1, c1, r2, c2):
    global result
    if(r2 == N - 1 and c2 == N - 1):
        result += 1
        return
    if(r2 == r1):
        if(c2 + 1 < N and maps[r2][c2 + 1] == 0):
            find_ways(r1, c1 + 1, r2, c2 + 1)
        if((c2 + 1 < N and r2 + 1 < N) and maps[r2][c2 + 1] == 0 and maps[r2+1][c2+1] == 0 and maps[r2 + 1][c2] == 0):
            find_ways(r1, c1 + 1, r2 + 1, c2 + 1)
    elif(c2 == c1):
        if(r2 + 1 < N and maps[r2 + 1][c2] == 0):
            find_ways(r1 + 1, c1, r2 + 1, c2)
        if((r2 + 1 < N and c2 + 1 < N) and maps[r2 + 1][c2] == 0 and maps[r2 + 1][c2 + 1] == 0 and maps[r2][c2 + 1] == 0):
            find_ways(r1 + 1, c1, r2 + 1, c2 + 1)
    else:
        if(c2 + 1 < N and maps[r2][c2 + 1] == 0):
            find_ways(r1 + 1,  c1 + 1, r2, c2 + 1)
        if(r2 + 1 < N and maps[r2 + 1][c2] == 0):
            find_ways(r1+1, c1 + 1, r2 + 1, c2)
        if((c2 + 1 < N and r2 + 1 < N) and maps[r2][c2 + 1] == 0 and maps[r2+1][c2+1] == 0 and maps[r2 + 1][c2] == 0):
            find_ways(r1 + 1, c1 + 1, r2 + 1, c2 + 1)


find_ways(0, 0, 0, 1)
print(result)
