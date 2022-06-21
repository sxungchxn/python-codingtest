import sys

sys.setrecursionlimit(10**7)


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())
M = int(readline())
if(M > 0):
    nobtns = list(map(int, readline().split(" ")))
else:
    nobtns = []

btns = []  # 사용 가능한 버튼들
min_dist = abs(N - 100)

for i in range(10):
    if i not in nobtns:
        btns.append(i)

btns.sort()


# curr = str, target = str, tar_len = int
def getDistance(curr, target, tar_len):
    global min_dist
    curr_len = len(curr)
    # min_dist check
    if curr_len > 0 and (curr_len >= tar_len - 1 and curr_len <= tar_len + 1):
        if curr_len != tar_len and curr[0] == "0":
            pass
        else:
            min_dist = min(min_dist, abs(
                int(curr) - int(target)) + len(str(int(curr))))
        if curr_len == tar_len + 1:
            return
    # recursive
    for btn in btns:
        getDistance(str(btn) + curr, target, tar_len)


if len(btns) == 10:
    min_dist = min(min_dist, len(str(N)))
elif len(btns) > 0:
    getDistance("", str(N), len(str(N)))
print(min_dist)
