import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())

nums = []

for i in range(N):
    num = int(readline())
    nums.append(num)

reversed = sorted(nums, reverse=True)


print(reversed)
