import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())
budgets = list(map(int, readline().split()))
limit = int(readline())

budgets.sort()

start = 0
end = budgets[-1]
max_upper = 0

while(start <= end):
    upper = (start + end) // 2
    check_sum = 0
    for budget in budgets:
        if budget <= upper:
            check_sum += budget
        else:
            check_sum += upper
    # check_sum이 상한선보다 작거나 같다[조건 만족] => 상한액을 올려도 된다
    if check_sum <= limit:
        max_upper = max(max_upper, upper)
        start = upper + 1
    # check_sum이 상한선 보다 크다 => 상한액을 내려야 한다
    else:
        end = upper - 1

print(max_upper, end='\n')
