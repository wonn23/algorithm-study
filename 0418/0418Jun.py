#백준0418 - 황준성



#---2798 – 블랙잭---



n, m = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= m:
                result = max(result, sum)

print(result)



#---2231 – 분해합---



n = int(input())

for i in range(1, n+1):
    digits_sum = i + sum(map(int, str(i)))
    if digits_sum == n:
        print(i)
        break
else:
    print(0)
