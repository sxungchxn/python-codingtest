import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())
nums = list(map(int, readline().split()))
nums.sort()

min_left = left = 0
min_right = right = N - 1
min_zero = nums[left] + nums[right]

while(left < right):
    sum = nums[left] + nums[right]
    if(abs(min_zero) > abs(sum)):
        min_left = left
        min_right = right
        min_zero = sum
    if sum > 0:
        # sum값 내리기
        right -= 1
    elif sum < 0:
        # sum값 올리기
        left += 1
    else:
        break

print(nums[min_left], nums[min_right])
