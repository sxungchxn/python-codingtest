num_set = set()

for num in range(1, 10001):
    result = num
    while num > 0:
        result += num % 10
        num = num // 10
    if result <= 10000:
        num_set.add(result)

for num in range(1, 10001):
    if num not in num_set:
        print(num, end='\n')
