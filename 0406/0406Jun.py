#백준0406 - 황준성



#---1904 – 01 타일---



n = int(input())

T = [0] * (n+1)        #인덱스 0은 사용하지 않고 1부터 시작
T[1] = 1

if n >= 2:
    T[2] = 2

for i in range(3, n+1):
    T[i] = (T[i-1] + T[i-2]) % 15746

# i-1 길이의 모든 2진 수열에서 마지막에 1을 추가한 경우의 수
# i-2 길이의 모든 2진 수열에서 마지막에 00을 추가한 경우의 수

print(T[n])



#100000007은 소수이긴 하지만 이 값으로 나누면
#나머지가 0이 되는 경우가 발생할 수 있습니다
#그리고 이 경우에는 잘못된 결과를 출력하게 됩니다
#반면에 15746은 소수가 아니지만 문제에서 주어진 조건 중 하나인
# "나머지를 출력한다"를 고려하면 15746으로 나누는 것이 올바른 방법입니다



#---1026 – 보물---



n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

S = 0
for i in range(n):
    S += A[i] * B[i]

print(S)



#---14495 – 피보나치 비스무리한 수열---



n = int(input())

fib_b = [1, 1, 1]     # f(1), f(2), f(3)

for i in range(3, n):
    fib_b.append(fib_b[i-1] + fib_b[i-3])

print(fib_b[n-1])