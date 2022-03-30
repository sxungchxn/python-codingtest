# False로 채워진 1차원 배열 할당
list1 = [False] * 9

print(list1)

# 빈 2차원 배열 할당
list2 = [[] for _ in range(5)]

print(list2)


# 0으로 채운 2차원 배열 할당
list3 = [[0 for col in range(11)] for row in range(10)]

print(list3)
