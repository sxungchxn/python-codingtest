import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())
nums = list(map(int, readline().split()))
K = int(readline())

nums.sort()
result = 0

for i in range(N):
    target = K - nums[i]
    left = i
    right = N - 1
    if target == nums[i]:
        continue
    while(left <= right):
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            result += 1
            break


print(result)
