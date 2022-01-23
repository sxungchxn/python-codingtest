n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

block_size = k + 1
block_sum = k * first + second
rest = m % block_size

result = m // block_size * block_sum + rest * first

print(result)


# [f, f, f, s]
