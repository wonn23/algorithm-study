### 0418 스터디~ 백준 문제 풀기
### 2231 - 분해합
n = int(input())

for m in range(1, n+1):
    x = m + sum(map(int, str(m)))
    if x == n:
        print(m)
        break
else:
    print(0)

### 2798 - 블랙잭
import itertools

n, limit = map(int, input().split())
arr = list(input().split(' '))
arr = [int(x) for x in arr]
comb = list(itertools.combinations(arr, 3))
blackjack = 0
for x in comb:
    if sum(x) > blackjack and sum(x) <= limit:
        blackjack = sum(x)

print(blackjack)



### 19532 - 수학은 비대면 강의입니다! 두 가지 방법으로 풀어 봤음..
## 692ms
a, b, c, d, e, f = map(int, input().split())
solution = []

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            solution = [x, y]
            break

print(solution[0], solution[1])



## 44ms
a, b, c, d, e, f = map(int, input().split())

x = (c*e-b*f)//(a*e-b*d)
y = (c*d-a*f)//(b*d-a*e)

print(x, y)