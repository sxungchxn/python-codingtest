a = int(input())
b = input()
b_reverse = b[::-1]  # start, stop, step

for num in b_reverse:
    result = a * int(num)
    print(result)

print(a * int(b))
