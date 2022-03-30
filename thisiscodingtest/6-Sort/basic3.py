import sys


def readline():
    return sys.stdin.readline().rstrip()


N = int(readline())

scores = []

for i in range(N):
    name, score = readline().split()
    scores.append((name, int(score)))


scores = sorted(scores, key=lambda score: score[0])

for info in scores:
    print(info[1], end=' ')
