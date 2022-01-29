import sys

count = int(sys.stdin.readline())

for i in range(0, count):
    result_line = sys.stdin.readline()
    line_score = 0
    mid_score = 1
    for result in result_line:
        if result == 'O':
            line_score += mid_score
            mid_score += 1
        else:
            mid_score = 1
    print(line_score)
