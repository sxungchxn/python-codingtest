array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 어느 한 요소를 기준으로 이전 요소보다 큰 경우 swap을 진행 하고 아니면 중지
# 이 과정을 모든 요소에 대해서 반복

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        # 정렬 순서가 잘 지켜져있으면 정렬과정 중단하기
        else:
            break
