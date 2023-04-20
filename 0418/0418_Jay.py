#2798 블랙잭
n, m = map(int, input().split()) 

cards = list(map(int, input().split())) 

result = 0 

for i in range(n): 
    for j in range(i+1, n): 
        for k in range(j+1, n):
            card_total = cards[i] + cards[j] + cards[k] 

            if card_total <= m and card_total >= result: 
                result = card_total

print(result) 

#2231 분해합

n = int(input())

for i in range(1, n+1): #자연수니까 1부터 시작
    if i + sum(map(int, str(i))) == n:
        print(i)
        break
else:
    print(0)

#19532 수학은 비대면 강의 입니다.

a, b, c, d, e, f = map(int, input().split())

x = (c * e - b * f) // (a * e - b * d) #크래머규칙 이용
y = (a * f - c * d) // (a * e - b * d)

print(x, y)
