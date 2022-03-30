# 어느 하나의 요소를 기준으로 잡는다
# 그 요소 다음 요소들 중 최소값을 찾는다
# 최소값 요소와 기준 요소를 서로 바꾼다
# 이 과정을 처음부터 끝까지의 요소에 대해 반복한다

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
