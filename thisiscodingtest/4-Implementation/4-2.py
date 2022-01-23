pos = input()


# ASCII 코드 변환
pos_x = ord(pos[0]) - ord('a') + 1
pos_y = int(pos[1])

mov_x = [2, 2, -2, -2, 1, 1, -1, -1]
mov_y = [1, -1, 1, -1, 2, -2, 2, -2]

# steps = [(2,1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

# print(pos_x, pos_y)

count = 0
for x, y in zip(mov_x, mov_y):
    if pos_x + x >= 1 and pos_x + x <= 8 and pos_y + y >= 1 and pos_y + y <= 8:
        count += 1

print(count)
