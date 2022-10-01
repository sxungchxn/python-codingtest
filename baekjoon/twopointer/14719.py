import sys

input = sys.stdin.readline

H, W = map(int, input().split())

Hs = list(map(int, input().split()))

width_sum = 0

for i in range(1, W - 1):
    left = [i - 1, Hs[i-1]]
    right = [i + 1, Hs[i + 1]]
    for l in range(i - 1, -1, -1):
        if Hs[l] > left[1]:
            left = [l, Hs[l]]
    for r in range(i+1, W):
        if Hs[r] > right[1]:
            right = [r, Hs[r]]
    value = min(left[1], right[1]) - Hs[i]
    if value > 0:
        width_sum += value

print(width_sum)
