import sys

sys.setrecursionlimit(int(1e9))


def readline():
    return sys.stdin.readline().rstrip()


N, M = map(int, readline().split(" "))
inputs = list(map(int, readline().split(" ")))
nums = []

for i in range(len(inputs)):
    if inputs[i] not in nums:
        nums.append(inputs[i])

nums.sort()
result = []


def recursive(length):
    global M, result
    if length == M:
        for num in result:
            print(num, end=' ')
        print()
    else:
        for num in nums:
            if len(result) == 0 or result[-1] <= num:
                result.append(num)
                recursive(length + 1)
                result.pop()


recursive(0)
