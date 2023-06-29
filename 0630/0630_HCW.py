# 네트워크
def solution(n, computers):
    def move(graph):  # [0,0]
        move_list = []
        for dx, dy in [-1, 0], [1, 0], [0, -1], [0, 1]:
            x = graph[0]
            y = graph[1]
            x += dx
            y += dy
            if 0 <= x < n and 0 <= y < n:
                move_list.append([x, y])
        return move_list

    visited = [[False for i in range(n)] for i in range(n)]
    network = 0
    for x in range(len(computers)):
        network += 1
        for y in range(len(computers)):
            stack = [comuters[x][y]]
            while stack:
                node = stack.pop()
                for dx, dy in node:
                    if visited[dx][dy] != True:
                        visited[dx][dy] = True
                        stack.extend(move([dx, dy]))
    return network


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
