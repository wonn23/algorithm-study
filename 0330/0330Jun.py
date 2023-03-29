#백준0330 - 황준성



#---설탕 배달---



n = int(input())

bag5 = n // 5  # 5kg 봉지 개수
bag3 = 0       # 3kg 봉지 개수

while bag5 >= 0:
    if (n - bag5 * 5) % 3 == 0:
        bag3 = (n - bag5 * 5) // 3
        break
    bag5 -= 1

if bag5 >= 0:
    print(bag5 + bag3)
else:
    print(-1)



#---게임을 만든 동준이---



n = int(input())
score = []
for i in range(n):
    score.append(int(input()))

count = 0
for i in range(n-2, -1, -1):
    if score[i] >= score[i+1]:
        count += score[i] - score[i+1] + 1
        score[i] = score[i+1]-1

print(count)



#---Pen Pineapple Apple Pen---



n = int(input())
s = input()
print(s.count('pPAp'))