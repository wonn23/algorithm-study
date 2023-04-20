### 1018 체스판 다시 칠하기
N, M = map(int, input().split())
board = []
answer = []
for i in range(N) :
    board.append(list(input()))

# print(N, M, board)

for x in range(N-7):
    for y in range(M-7):
        black = 0
        white = 0
        
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i+j)%2 == 0:
                    if board[i][j] == 'W':
                        black += 1
                    else: #board[i][j] == 'B':#
                        white += 1
                else:
                    if board[i][j] == 'W':
                        white += 1
                    else: #board[i][j] == 'B':#
                        black += 1
         
        answer.append(black)
        answer.append(white)

print(min(answer))



### 1436 영화감독 숌
N = int(input())
numbers = []
number = 666

while len(numbers) < N:
    if '666' in str(number):
        numbers.append(number)
    number += 1

print(numbers[-1])



### 14501 퇴사
N = int(input())
schedule = []
for _ in range(N):
    schedule.append(list(map(int, input().split())))

answer = [0] * (N+1)

for i in range(N):
    for j in range(i+schedule[i][0], N+1):
        if answer[j] < answer[i] + schedule[i][1]:
            answer[j] = answer[i] + schedule[i][1]
            
print(answer[-1])