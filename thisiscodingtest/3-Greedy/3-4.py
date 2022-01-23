n, k = map(int, input().split())

result = 0

while(True):
    rest = n % k
    n -= rest
    result += rest

    if n < k:
        break

    n = int(n / k)
    result += 1


result += (n - 1)
print(result)
