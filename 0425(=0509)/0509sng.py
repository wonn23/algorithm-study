################## 죽음의 게임
N, K = map(int, input().split())

num_list = [int(input()) for _ in range(N)]

target = 0  # 지목을 하는 사람 (0부터 시작)
M = 0

for i in range(N):
    target = num_list[target]
    M += 1
    if target == K:
        print(M)
        break
else:
    print(-1)
    
    
    
############## 영화감독 숌
N = int(input())
num = 666
count = 0

while(True):
    if '666' in str(num):
        count += 1
        
        if count == N:
            print(num)
            break
            
    num += 1
    
print(num)
