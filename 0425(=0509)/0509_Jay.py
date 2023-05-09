#숌
n = int(input())
count = 0
num = 665

while count < n:
    num += 1
    if '666' in str(num):
        count += 1

print(num)

#죽음의 게임
N, K= map(int,input().split())

#지목하는 사람의 번호 저장하기
death = []
for _ in range(N):
    death.append(int(input()))

target = 0
cnt = 0

for i in range(N):
    target = death[target]
    cnt+=1
    #보성이가 걸리면 끝
    if K==target:
        print(cnt)
        break
else:
    print(-1)