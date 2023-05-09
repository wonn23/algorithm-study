#백준0509 - 황준성



#---1018 – 체스판---



N, M = map(int, input().split())

board = []
for _ in range(N):
    row = input()
    board.append(row)

min_count = float('inf')  # 초기 최솟값 설정

for i in range(N-7):  # 시작 위치 i
    for j in range(M-7):  # 시작 위치 j
        # (i, j)부터 8x8 체스판 확인
        count1 = 0  # 맨 왼쪽 위 칸이 흰색인 경우 칠해야 하는 정사각형 개수
        count2 = 0  # 맨 왼쪽 위 칸이 검은색인 경우 칠해야 하는 정사각형 개수
        
        for x in range(i, i+8):
            for y in range(j, j+8):
                # 맨 왼쪽 위 칸이 흰색인 경우
                if (x + y) % 2 == 0:  # 행 번호와 열 번호의 합이 짝수인 경우
                    if board[x][y] != 'W':
                        count1 += 1
                    if board[x][y] != 'B':
                        count2 += 1
                # 맨 왼쪽 위 칸이 검은색인 경우
                else:  # 행 번호와 열 번호의 합이 홀수인 경우
                    if board[x][y] != 'B':
                        count1 += 1
                    if board[x][y] != 'W':
                        count2 += 1

        # 현재 체스판에서 다시 칠해야 하는 정사각형 개수의 최솟값 업데이트
        min_count = min(min_count, count1, count2)

print(min_count)



#---17204 – 죽음의게임---



N, K = map(int, input().split())

people = []
for _ in range(N):
    a = int(input())
    people.append(a)

for M in range(1, N+1):
    start = 0  # 현재 사람의 번호
    for _ in range(M):
        start = people[start]  # M번째 사람이 지목한 사람의 번호로 갱신
    
    if start == K:  # M번째 사람이 보성이일 경우
        print(M)
        break

if start != K:  # 보성이가 아니었을 경우
    print(-1)



#---1436 – 숌---



N = int(input()) 
count = 0 
number = 666 

while True:
    if '666' in str(number): 
        count += 1  
    if count == N:  
        print(number)
        break
    number += 1
