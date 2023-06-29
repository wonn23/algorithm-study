from collections import deque
import copy


def solution(rectangle, characterX, characterY, itemX, itemY):
    max_x = 0
    max_y = 0

    for x1, y1, x2, y2 in rectangle:
        max_x = max(max_x, x1, x2)  # 행
        max_y = max(max_y, y1, y2)  # 열

    # 0,0에서 시작이 아니므로 x,y좌표 1씩 늘려줌
    visited = [[0 for _ in range(max_y + 1)] for i in range(max_x + 1)]

    # visited를 깊은 복사로 완전 새롭게 복사함
    map = copy.deepcopy(visited)

    # 사각형 외각선 모두 1로 표현
    for i in range(len(rectangle)):
        x1 = rectangle[i][0]
        y1 = rectangle[i][1]
        x2 = rectangle[i][2]
        y2 = rectangle[i][3]
        for x in range(x1, x2 + 1):
            map[x][y1] = 1
            map[x][y2] = 1
        for y in range(y1, y2 + 1):
            map[x1][y] = 1
            map[x2][y] = 1

    # 사각형 내부에 있는 1을 0으로 바꿈
    for i in range(len(rectangle)):
        x1 = rectangle[i][0]
        y1 = rectangle[i][1]
        x2 = rectangle[i][2]
        y2 = rectangle[i][3]
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                map[x][y] = 0

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    distance = 0
    start = [characterX, characterY, distance]
    visited[characterX][characterY] = 1
    q.append(start)

    while q:
        x, y, distance = q.popleft()

        if x == itemX and y == itemY:
            return distance

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < max_x
                and 0 <= ny < max_y
                and not visited[nx][ny]
                and map[nx][ny] == 1
            ):
                visited[nx][ny] = 1
                q.append([nx, ny, distance + 1])

    return distance


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
