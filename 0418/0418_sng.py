#################### 2798 블랙잭

# 시도1 (108ms)
N, M = map(int, input().split())
cards = list(map(int, input().split()))
total = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= M:
                total.append(sum)
print(max(total))

# 시도2 (80ms)
N, M = map(int, input().split())
cards = list(map(int, input().split()))
total = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = cards[i] + cards[j] + cards[k]
            if (sum <= M) & (sum > total):
                total = sum
print(total)


#################### 2231 분해합
N = int(input())

for i in range(N):
    sum_inx = 0
    for j in str(i):
        sum_inx += int(j)
    if int(N) == sum_inx + i:
        print(i)
        break
else:
    print(0)
    
    
##################### 19532 수학은 비대면 강의입니다
a,b,c,d,e,f = list(map(int,input().split()))
values = []

# 대입 노가다 (x와 y를 -999부터 1000까지 모두 대입)
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c:
            values.append([x,y])

# 1행에서 얻은 x,y 묶음을 2행의 방정식에 대입해보면서 최종 해 찾기
for xy in values:
    if d*xy[0] + e*xy[1] == f:
        print(xy[0], xy[1])
        break