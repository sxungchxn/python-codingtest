import sys

N = int(sys.stdin.readline().rstrip())

count = 0


# [dict] 사용해서 풀기

# for i in range(0, N):
#     word = sys.stdin.readline().rstrip()
#     result = True
#     word_dict = dict()
#     for idx in range(0, len(word)):
#         if word_dict.get(word[idx]) is None:
#             word_dict[word[idx]] = 1
#         else:
#             if word[idx - 1] != word[idx]:
#                 result = False
#                 break
#     if result is True:
#         count += 1

# [set] 사용해서 풀기
for i in range(0, N):
    word = sys.stdin.readline().rstrip()
    result = True
    char_set = set()
    for idx in range(0, len(word)):
        if word[idx] in char_set:
            if word[idx - 1] != word[idx]:
                result = False
                break
        else:
            char_set.add(word[idx])
    if result is True:
        count += 1

print(count)
