import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())
nums = []
sum = 0


for i in range(N):
    num = int(readline())
    sum += num
    nums.append(num)

nums.sort()

# 산술 평균
avg = round(sum / N)
if avg > -1 and avg < 0.5:
    avg = 0
print(avg, end='\n')


# 중앙값
print(nums[N//2], end='\n')

# 최빈값
freq = 0
max_freq = 0
max_freqs = []
prev = value = 4001

for num in nums:
    if prev == num:
        freq += 1
    else:
        freq = 1
        prev = num
    if max_freq < freq:
        max_freq = freq
        value = num
        max_freqs = [num]
    elif max_freq == freq:
        max_freqs.append(num)

if len(max_freqs) > 1:
    print(max_freqs[1], end='\n')
else:
    print(max_freqs[0], end='\n')

# 범위(최대 - 최소)
print(nums[N-1] - nums[0])
