import sys


def readline():
    return sys.stdin.readline()


N = int(readline())
nums = []

for i in range(N):
    num = int(readline())
    nums.append(num)


nums.sort()
for num in nums:
    print(num, end='\n')
