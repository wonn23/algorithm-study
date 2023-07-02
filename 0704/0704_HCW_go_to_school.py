def solution(m, n, puddles):
    puddles = [[x, y] for y, x in puddles]  # puddles의 x,y 좌표 위치 바꿔주기

    map = [[0] * (m + 1) for _ in range(n + 1)]  # 1,1을 맞추기 위해서 한줄씩 더 늘림
    map[1][1] = 1
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if x == 1 and y == 1:  # map[1][1] = map[0][1] + map[1][0] = 0 + 0 = 0
                continue  # map[1][1] = 0 이되는 것을 막기위해서
            if [x, y] in puddles:
                map[x][y] = 0
            else:
                map[x][y] = (map[x - 1][y] + map[x][y - 1]) % 1000000007  # 문제 조건
    return map[n][m]


print(solution(5, 4, [[3, 2], [2, 4]]))
# map
# [0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1]
# [0, 1, 0, p, 0, 0]
# [0, 1, 0, 0, 0, 0]
# [0, 1, p, 0, 0, 0]
