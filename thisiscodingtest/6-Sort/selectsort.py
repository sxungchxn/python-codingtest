#

def selectsort(nums):
    length = len(nums)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


nums = [1, 3, 9, 2, 5, -2, -7]
nums = selectsort(nums)
print(nums)
