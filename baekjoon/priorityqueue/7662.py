import sys
import heapq


def readline():
    return sys.stdin.readline().rstrip()


T = int(readline())

# minQ, maxQ 두 개를 두기.

for _ in range(T):
    k = int(readline())
    maxh = []  # max heap
    minh = []  # min heap
    count = dict()
    for a in range(k):
        operator, operand = readline().split(" ")
        operand = int(operand)
        if operator == "I":
            heapq.heappush(minh, operand)
            heapq.heappush(maxh, -operand)
            if operand in count:
                count[operand] += 1
            else:
                count[operand] = 1
        else:
            if operand == 1 and maxh:
                # 최대값
                target = -maxh[0]
                if target in count:
                    heapq.heappop(maxh)
                    count[target] -= 1
                    if count[target] == 0:
                        del count[target]
            if operand == -1 and minh:
                target = minh[0]
                if target in count:
                    heapq.heappop(minh)
                    count[target] -= 1
                    if count[target] == 0:
                        del count[target]
            while maxh and -maxh[0] not in count:
                heapq.heappop(maxh)
            while minh and minh[0] not in count:
                heapq.heappop(minh)
    # print(count)
    if count:
        print(-maxh[0], minh[0])
    else:
        print("EMPTY")
