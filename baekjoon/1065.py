import sys


def check_hans(num):
    num_str = str(num)
    if len(num_str) == 1 or len(num_str) == 2:
        return True
    else:
        num_diff = int(num_str[0]) - int(num_str[1])
        no_han = False
        for i in range(1, len(num_str) - 1):
            diff = int(num_str[i]) - int(num_str[i+1])
            if num_diff != diff:
                no_han = True
                break
        if no_han is False:
            return True
        return False


X = int(sys.stdin.readline().rstrip())
han_count = 0

for num in range(1, X+1):
    if check_hans(num) is True:
        han_count += 1

print(han_count)
