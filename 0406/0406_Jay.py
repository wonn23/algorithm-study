###########14495 피보나치 비스무리한 수열
n = int(input())

if n == 1 or n == 2 or n == 3:
    print(1)
else:
    f1, f2, f3 = 1, 1, 1
    for i in range(4, n+1):
        fn = f1 + f3
        f3 = f2
        f2 = f1
        f1 = fn
    print(fn)

############## 1904 01타일
n = int(input())
    
Table = [0] * (1000001)
    
    # 초기값 설정
Table[1] = 1 
Table[2] = 2 
    
for i in range(3, 1000001):
    Table[i] = (Table[i-1] + Table[i-2]) % 15746
    
print(Table[n])

############### 1026 보물
n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

result = 0

for i in range(n):
    result += a[i] * b[i]

print(result)
