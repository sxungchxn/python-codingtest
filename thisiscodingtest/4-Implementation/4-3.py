
# map
# 0 : 육지, 1 : 바다, 2 : 가본 칸


whole_map = []
n = m = a = b = d = None

# direction
# 0 : 북, 1 : 동, 2 : 남, 3 : 서
# 반시계 방향 : 0 => 3 => 2 => 1 => 0 ...


def update_direction(d):
    new_d = d - 1
    if new_d < 0:
        new_d = 3
    return new_d


def get_pos(pos_n, pos_l, d, type=1):
    if d == 0:  # 북쪽
        return pos_n - 1 * type, pos_l
    elif d == 1:  # 동쪽
        return pos_n, pos_l + 1 * type
    elif d == 2:  # 남쪽
        return pos_n + 1 * type, pos_l
    else:  # 서쪽
        return pos_n, pos_l - 1 * type


if __name__ == '__main__':
    n, m = map(int, input().split())
    a, b, d = map(int, input().split())

    for i in range(n):
        row_map = list(map(int, input().split()))
        whole_map.append(row_map)

    visit = 1
    rotation = 0

    whole_map[a][b] = 2

    while(True):
        # print('loop')
        # 1단계 : 방향 업데이트
        d = update_direction(d)

        # 2단계
        new_n, new_l = get_pos(a, b, d)
        if(whole_map[new_n][new_l] == 0):
            # 이동하기
            a, b = new_n, new_l
            whole_map[a][b] = 2  # 방문 표시
            visit += 1
            rotation = 0  # 회전 횟수 초기화
        else:
            rotation += 1

        # 3단계
        if rotation == 4:
            back_n, back_l = get_pos(a, b, d, -1)
            if whole_map[back_n][back_l] == 1:
                break
            else:
                # 뒤로 이동하기
                a, b = back_n, back_l
                rotation = 0

    print(visit)
