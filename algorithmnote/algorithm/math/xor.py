# xor 연산자를 이용하면 linear한 시간복잡도와
# O(1) 공간복잡도로 배열 내에 혼자 있는 요소를 빠르게 찾을 수 있다.

nums = [1, 2, 1, 2, 5, 6, 7, 6, 7]

result = 0
for num in nums:
    result = result ^ num

print('혼자 있는 값 : ', result)
