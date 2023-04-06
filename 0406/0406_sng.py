######### 1904
N = int(input())

F = [0 for i in range(1000001)]
F[1] = 1
F[2] = 2

for i in range(3, N+1):
    F[i] = (F[i-2] + F[i-1]) % 15746

print(F[N])


##########14495
n = int(input())

F = [0 for i in range(117)]
F[1] = 1
F[2] = 1
F[3] = 1

for i in range(3, n+1):
    F[i] = F[i-3] + F[i-1]

print(F[n])


######### 1026
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

s = 0
for i in range(n):
    s = s + (A[i] * B[i])

print(s)