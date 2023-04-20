# 1018 체스판 다시칠하기
import sys
n,m = map(int,input().split())
chessboard = []
min_count = sys.maxsize

for i in range(n):
    chessboard.append(input())

for i in range(n-7):
    for j in range(m-7):
        start_W = 0 # W로 시작할 때
        start_B = 0 # B로 시작할 때
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2 == 0:
                    if chessboard[k][l] == 'W':
                        start_B += 1
                    if chessboard[k][l] == 'B':
                        start_W += 1
                elif (k+l)%2 == 1:
                    if chessboard[k][l] == 'W':
                        start_W += 1
                    if chessboard[k][l] == 'B':
                        start_B += 1
                    
        min_count = min(min_count,start_W,start_B)
        
print(min_count)

# 영화감독 숌

n = int(input())
num_list = [0]
index = 0
while len(num_list)<=n:
    if str(num_list[index]).count('666') >= 1:
        num_list.append(num_list[index])
        index += 1
        num_list[index] += 1
    else:
        num_list[index] += 1
print(num_list[-2])

# 퇴근

N = int(input())

T = [0] * (N+1)
P = [0] * (N+1)
Table = [0] * (N+2) 

for i in range(1, N+1):
    T[i], P[i] = map(int, input().split())

for i in range(N, 0, -1):
    if i + T[i] > N + 1:
        Table[i] = Table[i+1] 
    else:
        Table[i] = max(P[i] + Table[i+T[i]], Table[i+1]) 

print(Table[1])
