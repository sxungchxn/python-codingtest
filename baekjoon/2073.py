import sys

input = sys.stdin.readline

D, P = map(int, input().split())

pipes = []
for i in range(P):
    l, c = map(int, input().split())
    pipes.append((l, c))

pipes.sort(key=lambda x: (-x[0]))
# print(pipes)  # [0]: 길이, [1]: 용량

result = 0


# idx = 사용가능한 idx
# capcity = 남은 용량
def find_max(idx, rest_len, temp):
    global result
    if result != 0 and temp != 0 and temp <= result:
        return

    if rest_len == 0:
        if result == 0:
            result = temp
        else:
            result = max(result, temp)
        return
    if idx >= P:
        return
    for i in range(idx, len(pipes)):
        if rest_len >= pipes[i][0]:
            if temp == 0:
                find_max(i + 1, rest_len - pipes[i][0], pipes[i][1])
            else:
                find_max(i + 1, rest_len - pipes[i][0], min(pipes[i][1], temp))


find_max(0, D, 0)
print(result)
