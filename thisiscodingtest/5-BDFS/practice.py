# 스택 구현
from collections import deque
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)

stack.pop()


print(stack[::-1])  # 최상단 원소(top)부터 출력 => 3 - 2 - 5
print(stack)  # 5 - 2 - 3

# Queue 구현

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()  # 5 < 2 < 3 < 7 에서 5를 뺀다

queue.append(1)
queue.append(4)
queue.popleft()  # 2 < 3 < 7 < 1 <4 에서 2을 뺀다

print(queue)
queue.reverse()
print(queue)


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


print(factorial(10))
