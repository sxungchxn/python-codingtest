import sys

sys.setrecursionlimit(int(1e9))


def readline():
    return sys.stdin.readline().rstrip()


N, M = map(int, readline().split(" "))
nums = list(map(int, readline().split(" ")))

nums.sort()

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
        if len == 0 or nums[i] >= temp[len - 1]:
            temp.append(nums[i])
            rotate(len + 1)
            temp.pop()


rotate(0)
