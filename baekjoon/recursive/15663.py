import sys

sys.setrecursionlimit(int(1e9))


def readline():
    return sys.stdin.readline().rstrip()


N, M = map(int, readline().split(" "))
nums = list(map(int, readline().split(" ")))

used = [False] * N

result = []

results = {}

nums.sort()


def numToKey(nums):
    result = ''
    for num in nums:
        result += str(num)
        result += ' '
    return result


def recursive(len):
    global M, result
    if len == M:
        key = numToKey(result)
        if key not in results:
            results[key] = 1
            for num in result:
                print(num, end=' ')
            print()
    else:
        for i in range(N):
            if used[i] == False:
                used[i] = True
                result.append(nums[i])
                recursive(len + 1)
                result.pop()
                used[i] = False


recursive(0)
