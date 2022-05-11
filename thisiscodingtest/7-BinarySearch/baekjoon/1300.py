import sys
# import time


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())
K = int(readline())

# start_time = time.time()
limit = N * N
start = 1
end = limit
result = limit

while(start <= end):
    mid = (start + end) // 2
    count = 0
    for i in range(1, N+1):
        count += min(N, mid // i)
    if count >= K:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result, end='\n')
# print(time, time.time() - start_time)
