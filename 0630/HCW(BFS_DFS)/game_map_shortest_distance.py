from collections import deque


def solution(maps):
    n = len(maps)  # 행
    m = len(maps[0])  # 열

    visited = [[False for i in range(m)] for j in range(n)]  # 2D로 방문 행렬 초기화

    q = deque()
    x, y, distance = 0, 0, 1  # x,y 위치와 distance 초기화(제자리 시작인 것도 거리 1 세어줘야함)
    q.append(x, y, distance)
    visited[0][0] = True

    while q:
        x, y, distance = q.popleft()
        if x == n - 1 and y == m - 1:  # x,y가 도착지점에 도달했는지 먼저 확인하는 것이 중요하다
            return distance

    return -1  # while을 모두 빠져나왔다는 것은 도착지점에 도달 못했다는 것을 의미한다


print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1],
        ]
    )
)
