import sys

sys.setrecursionlimit(int(1e9))


def readline():
    return sys.stdin.readline().rstrip()


N, M = map(int, readline().split(" "))
nums = list(map(int, readline().split(" ")))

nums.sort()

# [1, 7, 8, 9]

temp = []
visited = [False] * N


def rotate(len):
    global N, M, temp, nums
    if len == M:
        for tmp in temp:
            print(tmp, end=' ')
        print()
        return
    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            temp.append(nums[i])
            rotate(len + 1)
            temp.pop()
            visited[i] = False


rotate(0)
