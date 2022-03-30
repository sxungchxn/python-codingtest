# 주어진 배열에서 첫번째 요소를 기준값 (pivot)으로 삼는다.
# pivot 보다 큰 값의 인덱스(left)를 왼쪽 끝에서부터 탐색
# pivot 보다 작은 값의 인덱스(right)를 오른쪽 끝에서부터 탐색
# left < right 인 경우 left, right를 서로 swap 해준다

# 위와 달리 left와 right가 역전된 경우에는 pivot과 right를 swap해준다 => 이후에는 이러한 탐색 과정을 종료한다

# 탐색과정을 종료되었을때 배열이 pivot을 기준으로 왼쪽으로 정렬된 부분, 오른쪽으로 정렬된 부분으로 나뉘는데 이 두 부분에 대하여
# 위 과정을 재귀적으로 반복해준다.(단 start < end 일때까지만 지속하기)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


# def quick_sort(array, start, end):
#     # start >= end (array 내에서 숫자의 개수가 1개라는 의미) 되면 quick_sort 종료
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#     while(left <= right):
#         # pivot보다 큰 값 찾기
#         while(left <= end and array[left] <= array[pivot]):
#             left += 1
#         # pivot보다 작은 값 찾기
#         while(right > start and array[right] >= array[pivot]):
#             right -= 1

#         # left와 right가 엇갈린 경우 => pivot <> right => 결과적으로 array[right]에는 pivot값이 위치
#         if left > right:
#             array[pivot], array[right] = array[right], array[pivot]
#         else:  # 엇갈리지 않고 제대로 찾은 경우
#             array[left], array[right] = array[right], array[left]

#     quick_sort(array, start, right - 1)
#     quick_sort(array, right + 1, end)


# 간결한 버전
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


# quick_sort(array, 0, len(array) - 1)

print(quick_sort(array))
# print(array)
