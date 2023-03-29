#0330 스터디_ 백준

# 설탕 배달 #####
n = int(input())

sugar = 0 # 설탕 봉지 개수

while n>0:
    if n%5 == 0:
        sugar += n//5
        break
    elif n==1 or n==2:
        sugar = -1
        break
    else:
        n -= 3
        sugar += 1
        
print(sugar)


# 게임을 만든 동준이 #####
level = int(input()) # 입력받은 수만큼 레벨 생성
Score = []
for i in range(level):
    Score.append(int(input())) # level 만큼 점수 배열에 점수 append

count = 0
for i in range(1, level) :
    #if Score[i+1] <= Score[i]:
        # count += Score[i] - Score[i+1] + 1
        # Score[i] = Score[i+1] - 1
        # 이미 지나간 인덱스에 대해서는 정리가 안됨 . .
    
    if Score[-i] <= Score[-i-1] : 
        count += Score[-i-1] - Score[-i] + 1 
        Score[-i-1] = Score[-i] - 1 
        #조건 ) 정답이 여러 가지인 경우에는 점수를 내리는 것을 최소한으로 하는 방법을 찾아야 한다.

print(count)


#pPAp
find = 'pPAp'

n = int(input())
str1 = input()
count = 0
str3 = list(str1)

for i in range(n) :
    str2 = str3[i:i+4]
    
    if find == ''.join(str2):
        count+=1
        str3[i+3] = 'o'

print(count)