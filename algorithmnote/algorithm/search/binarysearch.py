from bisect import bisect_left, bisect_right


# 재귀문
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if target == array[mid]:
        return mid
    elif target > array[mid]:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

# 반복문
# def binary_search(array, target, start, end):
#     while(start < end):
#         mid = (start + end) // 2

#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None


a = [1, 2, 4, 4, 8]
x = 4

# 이진 탐색을 통해 x가 들어갈 가장 왼쪽의 인덱스를 반환 = 가장 왼쪽에 있는 x의 위치 반환, 없으면 배열의 길이 반환
print(bisect_left(a, x))  # 2
# 이진 탐색을 통해 x가 들어갈 가장 오른쪽의 인덱스를 반환 = 가장 오른쪽에 있는 x의 위치 반환, 없으면 배열의 길이 반환
print(bisect_right(a, x))   # 4


# [left_value, right_value] 범위에 해당하는 값들의 개수
# [left_value, right_value]에 해당하는 값이 없으면 bisect_left, bisect_right는 같은 값을 반환.
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4))

print(count_by_range(a, -1, 3))
