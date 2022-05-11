from collections import deque

d = deque()
print(type(d))

# 덱의 오른쪽에서 새로운 요소들 삽입
for i in range(10):
    d.append(i)
print(d)

d.appendleft(10)
print(d)

# 덱 중간에 요소 삽입
d.insert(5, 11)
print(d)

# 덱 왼쪽/오른쪽에 iterable한 객체를 통째로 append하여 연장 : extendleft / extend
d.extend([0, 0, 0])
print(d)
d.extendleft([0, 0, 0])

# 오른쪽에서 부터 요소 제거
for i in range(10):
    d.pop()
print(d)

# 왼쪽에서 부터 요소 제거
for i in range(3):
    d.popleft()

print(d)

# 일반적인 리스트로 이용 가능
print(list(d))
