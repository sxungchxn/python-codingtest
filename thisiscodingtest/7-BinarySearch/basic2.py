import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

sys.setrecursionlimit(10000000)

N, M = map(int, input().split())

nums = list(map(int, input().split()))

left_index = bisect_left(nums, M)
right_index = bisect_right(nums, M)


if left_index >= N:
    print(-1)
else:
    print(right_index - left_index)
# if nums[left_index] != M or nums[right_index] != M:
# print(left_index, right_index)
