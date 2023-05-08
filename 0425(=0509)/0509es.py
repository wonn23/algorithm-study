#0425 은석 !! 1018, !1436,  14501, !17204, 9251

#1018 체스판 

n, m = map(int, input().split());

chessboard = []


for _ in range(n):
    chessboard.append(input())
#print(chessboard[0][0])
cnt=[]
for i in range(n-7):
    for j in range(m-7):
        Wboard = 0
        Bboard = 0
        for a in range(i,i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if chessboard[a][b] != 'W':
                        Wboard += 1
                    else:
                        Bboard += 1
                else :
                    if chessboard[a][b] != 'W':
                        Bboard += 1
                    else:
                        Wboard += 1
        cnt.append(Bboard);
        cnt.append(Wboard)
print(min(cnt))



#1436 영화감독
n = int(input())
jongmal = 665
cnt = 1

while cnt<=n:
    if '666' in str(jongmal):
        cnt+=1
    jongmal+=1

print(jongmal - 1)



#17204 더겜오브데스
N, K= map(int,input().split())
death = []
for _ in range(N):
    death.append(int(input()))

target = 0
cnt = 0
for i in range(N):
    target = death[target]
    cnt+=1
    if K==target:
        print(cnt)
        break
else:
    print(-1)