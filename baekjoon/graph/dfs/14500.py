import sys


def readline():
    return sys.stdin.readline().rstrip()


N, M = map(int, readline().split(" "))

nums = []

for _ in range(N):
    nums.append(list(map(int, readline().split(" "))))

max_sum = 0

# downward block
for i in range(M):
    for j in range(N - 1):
        # j = start point
        # works for length 2
        # calc 2 block sum
        if j == 0:
            sum = 0
            for k in range(j, j+2):
                sum += nums[k][i]
            sum3 = sum  # sum3 생성
        else:
            sum = sum - nums[j-1][i] + nums[j+1][i]

        # works for length 2
        # part 2
        if i - 1 >= 0 and i + 1 < M:
            max_sum = max(max_sum, sum + nums[j][i-1] + nums[j+1][i+1])
            max_sum = max(max_sum, sum + nums[j][i+1] + nums[j+1][i - 1])

        # part 1 left
        if i - 1 >= 0:
            temp_sum = sum + nums[j][i-1]
            if j - 1 >= 0:
                max_sum = max(max_sum, temp_sum + nums[j-1][i-1])
            max_sum = max(max_sum, temp_sum + nums[j + 1][i-1])
            if j + 2 < N:
                max_sum = max(
                    max_sum, sum + nums[j + 1][i - 1] + nums[j+2][i-1])

        # part1 right
        if i + 1 < M:
            temp_sum = sum + nums[j][i+1]
            if j - 1 >= 0:
                max_sum = max(max_sum, temp_sum + nums[j-1][i+1])
            max_sum = max(max_sum, temp_sum + nums[j + 1][i+1])
            if j + 2 < N:
                max_sum = max(
                    max_sum, sum + nums[j + 1][i + 1] + nums[j+2][i+1])

        # works for length 3
        if j < N - 2:
            # calc 3 block sum
            if j == 0:
                sum3 += nums[j+2][i]
            else:
                sum3 = sum3 - nums[j-1][i] + nums[j + 2][i]
            # add options
            # upside
            if j - 1 >= 0:
                max_sum = max(max_sum, sum3 + nums[j - 1][i])
            # downside
            if j + 3 < N:
                max_sum = max(max_sum, sum3 + nums[j + 3][i])
            # leftside
            if i - 1 >= 0:
                for k in range(j, j+3):
                    if k < N:
                        max_sum = max(max_sum, sum3 + nums[k][i - 1])
            # rightside
            if i + 1 < M:
                for k in range(j, j+3):
                    if k < N:
                        max_sum = max(max_sum, sum3 + nums[k][i + 1])

# len = 3 rightward block
for i in range(N):
    for j in range(M - 2):
        # j = start point
        if j == 0:
            sum = 0
            for k in range(j, j + 3):
                sum += nums[i][k]
        else:
            sum = sum - nums[i][j - 1] + nums[i][j + 2]
        # add options
        # left side
        if j - 1 >= 0:
            max_sum = max(max_sum, sum + nums[i][j-1])
        # right side
        if j + 3 < M:
            max_sum = max(max_sum, sum + nums[i][j+3])
        # up side
        if i - 1 >= 0:
            for k in range(j, j+3):
                if k < M:
                    max_sum = max(max_sum, sum + nums[i - 1][k])
        # down side
        if i + 1 < N:
            for k in range(j, j+3):
                if k < M:
                    max_sum = max(max_sum, sum + nums[i + 1][k])


# len = 2

print(max_sum)
