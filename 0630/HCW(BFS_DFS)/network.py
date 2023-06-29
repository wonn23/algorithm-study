def solution(n, computers):
    def dfs(x):  # 왜 2차원이 아니라 1차원으로 풀 수 있는걸까?
        stack = []
        stack.append(x)
        while stack:
            node = stack.pop()
            for y in range(n):
                if computers[node][y] == 1 and visited[y] == False:
                    visited[y] = True
                    stack.append(y)

    visited = [False for _ in range(n)]
    network = 0
    for i in range(n):
        if visited[i] == False:
            network += 1
            visited[i] = True
            dfs(i)
    return network


print(
    solution(
        7,
        [
            [1, 1, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 1, 0],
            [1, 0, 0, 0, 0, 0, 1],
        ],
    )
)
