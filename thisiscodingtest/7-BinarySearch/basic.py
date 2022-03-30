import sys
from bisect import bisect_left, bisect_right


def readline():
    return sys.stdin.readline().rstrip()


N, M = map(int, readline().split())

dducks = list(map(int, readline().split()))

dducks.sort()

min_val = 0
max_val = dducks[-1]
max_cmp = 0

while(min_val <= max_val):
    cmp = (min_val + max_val) // 2
    cmp_sum = 0
    left_idx = bisect_left(dducks, cmp)
    for dduck in dducks:
        if dduck > cmp:
            cmp_sum += (dducks - cmp)
    if cmp_sum >= M:
        # cmp_sum 증가 => min 값 변경
        min_val = cmp + 1
        max_cmp = max(cmp, max_cmp)
    else:
        # cmp_sum 감소 => max 값 변경
        max_val = cmp - 1

print(max_cmp, end='\n')
