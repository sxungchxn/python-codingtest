import sys


def readline():
    return sys.stdin.readline().rstrip()


N, S = map(int, readline().split())
nums = list(map(int, readline().split()))

left = 0
right = 0
min_len = N + 1
sum = nums[0]

while(True):
    if sum >= S:
        min_len = min(right - left + 1, min_len)
    if left < right:
        if sum < S:
            if right + 1 >= N:
                break
            right += 1
            sum += nums[right]
        else:
            sum -= nums[left]
            left += 1
    else:
        if right + 1 < N:
            sum += nums[right + 1]
            right += 1
        else:
            break

while left < N:
    sum -= nums[left]
    if sum >= S:
        min_len = min(right-left+1, min_len)
    left += 1

result = 0
if min_len < N + 1:
    result = min_len
print(result)
