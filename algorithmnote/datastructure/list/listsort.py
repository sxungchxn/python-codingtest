a = [1, 7, 5, 6, 1]
b = [1, 7, 5, 6, 1]

# 순서대로 정렬
a.sort()
print(a)

# 반대로 정렬
a.reverse()
print(a)

# 본체는 건드리지 않고 정렬
b_sorted = sorted(b)

# 단순히 앞뒤로 뒤집기
b_reversed = list(reversed(b))

print(b)
print(b_sorted)
print(b_reversed)

# lambda를 활용
# lambda = 함수의 간탄한 형태
#
# def func(x):      =   lambda x:x+10
#   return x + 10
#
# tuple list의 활용
tuple_list = [('lee', 55), ('kim', 12), ('park', 25)]

tuple_list.sort(key=lambda item: item[1])

print(tuple_list)

reverse_list = sorted(tuple_list, key=lambda x: x[1], reverse=True)
print(reverse_list)
