graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9

# 스택이나 재귀 함수를 이용

# 재귀 함수
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=' ')
#     for n_v in graph[v]:
#         if visited[n_v] == False:
#             dfs(graph, n_v, visited)


# 스택 활용
def dfs(graph, start, visited):
    stack = [start]
    visited[start] = True
    print(start, end=' ')
    while(stack):
        top = stack[- 1]
        all_visited = True
        for n_v in graph[top]:
            if not visited[n_v]:
                all_visited = False
                stack.append(n_v)
                visited[n_v] = True
                print(n_v, end=' ')
                break
        if all_visited:
            stack.pop()


dfs(graph, 1, visited)
