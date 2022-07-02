import sys
from bisect import bisect_left, bisect_right


def readline():
    return sys.stdin.readline().rstrip()


def binary_left(nums, target):
    left = 0
    right = len(nums) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result


def binary_right(nums, target):
    left = 0
    right = len(nums) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result


L = int(readline())

nums = list(map(int, readline().split(" ")))
nums.sort()  # 포함되면 안되는 숫자들
n = int(readline())

if n in nums:
    print(0)
else:
    left_idx = binary_left(nums, n)
    right_idx = binary_right(nums, n)
    p_l = 1 if left_idx == -1 else nums[left_idx] + 1
    p_r = 1000 if right_idx == -1 else nums[right_idx] - 1
    result = 0

    right_cnt = (n - 1 - p_l + 1) * (p_r - n + 1)
    if right_cnt > 0:
        result += right_cnt
    left_cnt = (p_r - (n + 1) + 1)
    if left_cnt > 0:
        result += left_cnt
    print(result)
