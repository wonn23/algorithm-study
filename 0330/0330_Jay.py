################# 설탕배달

n = int(input()) #상근이가 배달해야할 Nkg 설탕 무게

noAns = -1 

for fiveCount in range(n//5, -1, -1):
    threeCount = (n - fiveCount*5) // 3
    if fiveCount*5 + threeCount*3 == n:
        print(fiveCount + threeCount)
        break
else:
    print(noAns)

#################### 게임을 만든 동준이

lv = int(input())
score = []
for i in range(lv):
   score.append(int(input()))

count = 0

for i in range(lv-1, 0, -1):
  if score[i] <= score[i-1]:
    count += score[i-1] - score[i] + 1
    score[i-1] = score[i] - 1
print(count)

####################### pen Pineapple Apple pen

n = int(input())
str = input()
word = "pPAp"
print(str.count(word))