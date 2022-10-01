import sys

input = sys.stdin.readline

T = int(input().rstrip())

alpha_len = ord('z') - ord('a') + 1


for t in range(T):
    W = input().rstrip()

    K = int(input().rstrip())
    if(K == 1):
        print(1, 1)
    else:
        length = len(W)
        min_len = 99999
        max_len = -1

        count = [[] for i in range(alpha_len)]
        for i in range(length):
            count_idx = ord(W[i]) - ord('a')
            count[count_idx].append(i)

        for alpha_idx in range(alpha_len):
            alpha_cnt_len = len(count[alpha_idx])
            if len(count[alpha_idx]) >= K:
                # 최소 길이
                for i in range(alpha_cnt_len - (K - 1)):
                    diff = count[alpha_idx][i+K - 1] - count[alpha_idx][i] + 1
                    min_len = min(min_len, diff)
                    max_len = max(max_len, diff)
        if max_len == -1:
            print(-1)
        else:
            print(min_len, max_len)
