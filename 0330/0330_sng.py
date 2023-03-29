################# 설탕배달

sugar = int(input())
bagCount = 0

if sugar % 5 == 0:
    bagCount = bagCount + (sugar//5)
    print(bagCount)
else:
    while(True):
        sugar = sugar - 3
        bagCount += 1
        if sugar % 5 == 0:     # 3kg과 5kg를 조합해서 담을 수 있을 때
            bagCount = bagCount + (sugar//5)
            print(bagCount)
            break
        elif (sugar > 0) and (sugar <= 2):   # 나눠지지 않는 경우
            print(-1)
            break
        elif sugar == 0:   # sugar가 애초에 3KG이었을 때
            print(bagCount)
            break
        
        
        
################ 게임 동준이

N = int(input())
score = []
for i in range(N):
    score.append(int(input()))

count = 0
for i in range(N-2, -1, -1):
    if score[i] >= score[i+1]:
        count = count + (score[i] - score[i+1] + 1)
        score[i] = score[i+1] - 1

print(count)


################ 펜파인애플애플펜

N = int(input())
str = input()
word = 'pPAp'
print(str.count(word))