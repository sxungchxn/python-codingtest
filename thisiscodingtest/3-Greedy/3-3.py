n, m = map(int, input().split())

min_max = 1

for i in range(0, n):
    row = list(map(int, input().split()))
    # row.sort()
    # row_min = row[0]\
    row_min = min(row)
    # if(row_min > min_max):
    #     min_max = row_min
    min_max = max(row_min, min_max)

print(min_max)
