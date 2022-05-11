import sys
from bisect import bisect_left, bisect_right


def readline():
    return sys.stdin.readline().rstrip()


N, M = map(int, readline().split())
nums = list(map(int, readline().split()))
cnt = [0] * M

for i in range(0, N):
    if i > 0:
        nums[i] += nums[i-1]
    rest = nums[i] % M
    cnt[rest] += 1

res = cnt[0]
for i in range(0, M):
    if cnt[i] > 0:
        res += (cnt[i] * (cnt[i] - 1)) // 2

print(res)

# 모듈러 성질
# (A - B) % N = (A % N - B % N) % N = 0

# 특정 구간의 합 : [i, j] = sums[j] - sums[i - 1] (i <= j, i >= 1)
# 모듈러 성질에 의해 (sums[j] - sums[i - 1]) % N == sums[j] % N - sums[i - 1] % N = 0
# 찾으려는 것 :
# 1. sums[j] % N = sums[i-1] % N 인 것들
# 2. sums[j] % N = 0인 것들
