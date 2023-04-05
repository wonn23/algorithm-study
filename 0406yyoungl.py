## 백준 1026 보물
## 면접 이슈로 이것만 일단 커밋하고 시간 될 때 하겠습니다 ^^ ...
## 문제가 어이없는 포인트: B는 재배열하면 안 된다고 했는데 그럼 왜? s 최솟값만 출력하라고 한 건지......
## 만약 제대로 하려면 s를 배열로 구한 후 a를 b에 맞춰서 재배열하는 방법으로 해야 하나??


n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

s = 0

sortedA = sorted(a, reverse=True)
sortedB = sorted(b)

for x in range(n):
    s += sortedA[x] * sortedB[x]

print(s)