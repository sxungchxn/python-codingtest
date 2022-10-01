import sys

input = sys.stdin.readline

A, B = map(int, input().rstrip().split())
num = B
cnt = 0

while(A <= num):
    if(A == num):
        break
    elif(num % 2 == 0):
        num = num // 2
        cnt += 1
    elif(str(num)[-1] == '1'):
        num = int(str(num)[:-1])
        cnt += 1
    else:
        cnt = 0
        break
if(A == num):
    print(cnt + 1)
else:
    print(-1)
