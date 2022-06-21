import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())
M = int(readline())
S = readline()

tokens = S.split("I")
count = 0
result = 0
for i in range(1, len(tokens) - 1):
    if tokens[i] == 'O':
        count += 1
    else:
        if count >= N:
            result += (count - N) + 1
        count = 0

if count >= N:
    result += (count - N) + 1
print(result)

# split 하여 얻은 토큰이 O인 것을 카운트하면 끝

# 첫번째 토큰은 어떠한 경우에도 해당되지않음
# OIOI => [O, O, '']
# 마지막 토큰도 해당되지 않음
# OIOIO => [O, O, Oa];
