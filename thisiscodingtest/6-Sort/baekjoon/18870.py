import sys


def readline():
    return sys.stdin.readline()


num_set = set()
nums = []
N = int(readline())


nums = list(map(int, readline().split()))

# 숫자들이 한번만 들어간 집합 생성
for num in nums:
    num_set.add(num)

# 집합의 아이템들을 리스트에 담은 뒤 정렬
order_nums = []
for item in num_set:
    order_nums.append(item)
order_nums = sorted(order_nums)

# dict 생성 후 숫자들에 대한 정렬 정보를 dict에 저장
order_dict = dict()
for i in range(len(order_nums)):
    order_dict[order_nums[i]] = i

for i in range(len(nums)):
    if i == len(nums) - 1:
        print(order_dict[nums[i]], end='\n')
    else:
        print(order_dict[nums[i]], end=' ')
