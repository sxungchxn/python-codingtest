import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

# sys.setrecursionlimit(10000000)


def countRange(all_nums, val):
    left_index = bisect_left(all_nums, val)
    right_index = bisect_right(all_nums, val)
    # print(right_index, left_index, end='\n')
    return right_index - left_index


N = int(input())
all_nums = list(map(int, input().split()))
all_nums.sort()
# print('all_nums : ', all_nums, end='\n')

M = int(input())
count_nums = list(map(int, input().split()))


for count_num in count_nums:
    print(countRange(all_nums, count_num), end=' ')
