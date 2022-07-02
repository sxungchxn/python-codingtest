import sys


def readline():
    return sys.stdin.readline().rstrip()


T = int(readline())


for _ in range(T):
    N = int(readline())
    dp = [[0 for _ in range(N)] for i in range(2)]
    stickers = []
    for i in range(2):
        sticker_line = list(map(int, readline().split(" ")))
        stickers.append(sticker_line)

    for col in range(N):
        for row in range(2):
            target_row = 0 if row == 1 else 1
            c1 = c2 = c3 = c4 = 0
            if col - 1 >= 0:
                c1 = dp[target_row][col - 1]
                c4 = dp[row][col - 1]  # [row][col] 번째를 포함하지 않는 경우도 고려
            if col - 2 >= 0:
                c2 = dp[row][col - 2]
                c3 = dp[target_row][col - 2]
            dp[row][col] = max(stickers[row][col] + max(c1, c2, c3), c4)
    print(max(dp[0][N - 1], dp[1][N - 1]))

# 50 40  200 120 160
# 30 100 120 110 260


# 10 50 60 130 210 210 270
# 20 50 80 110 190 230 290
