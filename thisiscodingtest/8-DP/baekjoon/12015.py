import sys
from bisect import bisect_left, bisect_right


def readline():
    return sys.stdin.readline().rstrip()


# find lower bound => start를 target에 최대한 딱 맞게 붙인다
def binary_search(target, nums, start, end):
    while(start <= end):
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


N = int(readline())
nums = list(map(int, readline().split()))

dp = []
dp.append(nums[0])


for i in range(1, N):
    if dp[-1] < nums[i]:
        dp.append(nums[i])
    else:
        # binary_index = binary_search(nums[i], dp, 0, len(dp) - 1)
        dp[bisect_left(dp, nums[i])] = nums[i]

print(len(dp))
