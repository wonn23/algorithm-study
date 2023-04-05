### 1904번 01타일 ###

# 엘리스 줄세우기 문제와 같은 것이더군요. 한달전에는 어려웠는데 나도 이제 알고리즘 고수?!
n = int(input())
Table = [0]*(1000000+1)
Table[1] = 1
Table[2] = 2
for i in range(3,1000001):
    Table[i] = (Table[i-2] + Table[i-1])%15746

print(Table[n])

### 1026번 보물 ###

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

result = 0

A = sorted(A)
C = sorted(B,reverse =True) # B를 재배열한 것이 아니라 B와같은 C를 재배열한 것이다!!!
for i in range(n):
    result+=A[i]*C[i]
print(result)

### 14495번 피보나치 비스무리한 수열 ###

def similar_fibonach(n):
    if n<=3:
        return 1
    else:
        sfibo = [0] * n
        sfibo[0] = 1
        sfibo[1] = 1
        sfibo[2] = 1

        for i in range(3,n):
            sfibo[i] = sfibo[i-3] + sfibo[i-1]
        return sfibo[n-1]
n = int(input())
print(similar_fibonach(n))