import sys
input = sys.stdin.readline
LEFT = 0
MID = 1
RIGHT = 2
MAX = 9999999


N, M = map(int, input().split())

nums = []
prev_min = [[MAX] * 3 for col in range(M)]
next_min = [[MAX] * 3 for col in range(M)]


for i in range(N):
    num_list = list(map(int, input().split()))
    nums.append(num_list)

for col in range(M):
    for i in range(3):
        prev_min[col][i] = nums[0][col]


for row in range(1, N):
    for col in range(M):
        if col == 0:
            next_min[col] = [MAX, prev_min[col][RIGHT] + nums[row][col],
                             min(prev_min[col + 1][LEFT], prev_min[col + 1][MID]) + nums[row][col]]
        elif col == M - 1:
            next_min[col] = [min(prev_min[col - 1][RIGHT], prev_min[col - 1][MID]) +
                             nums[row][col], prev_min[col][LEFT] + nums[row][col], MAX]
        else:
            next_min[col] = [
                min(prev_min[col-1][MID], prev_min[col-1]
                    [RIGHT]) + nums[row][col],
                min(prev_min[col][LEFT], prev_min[col]
                    [RIGHT]) + nums[row][col],
                min(prev_min[col+1][MID], prev_min[col+1]
                    [LEFT]) + nums[row][col]
            ]
    prev_min = next_min.copy()

result = MAX
for col in range(M):
    for i in range(3):
        result = min(result, next_min[col][i])
print(result)
