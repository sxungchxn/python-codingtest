from collections import deque, Counter

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))


counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))
