import sys


def readline():
    return sys.stdin.readline()


N = int(readline())
nums = []

for i in range(N):
    num = int(readline())
    nums.append(num)


# 5 3 2 1 4

for i in range(N):
    min_index = i
    for j in range(i+1, N):
        if nums[min_index] > nums[j]:
            min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]


for num in nums:
    print(num, end='\n')
