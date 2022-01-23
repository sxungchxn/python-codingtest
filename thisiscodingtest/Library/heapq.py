import heapq
from typing import List


def heapsort(iterable: List[int]) -> List[int]:
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)

    for _ in range(len(h)):
        result.append(heapq.heappop(h))

    return result


def heapdownsort(iterable: List[int]) -> List[int]:
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)

    for _ in range(len(h)):
        result.append(-1 * heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
result = heapdownsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
