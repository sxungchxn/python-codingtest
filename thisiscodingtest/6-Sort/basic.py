import sys


def readline():
    return sys.stdin.readline().rstrip()


N, K = map(int, readline().split())

list_a = list(map(int, readline().split()))
list_b = list(map(int, readline().split()))


list_a.sort()
list_b.sort()

print(list_a)
print(list_b)

for i in range(K):
    max_idx = N - 1 - i
    min_idx = i
    list_a[min_idx], list_b[max_idx] = list_b[max_idx], list_a[min_idx]


print(list_a)
print(list_b)

print(sum(list_a))
