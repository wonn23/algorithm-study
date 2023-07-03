# 문제의 목표: N을 최소로 사용해서 주어진 number 만들기!
# 동적계획법 : 계산한 연산의 값을 저장해 두어서, 중복되는 연산은 저장한 값을 쓴다. 모든 경우의 수를 검토하여 최적의 해를 찾는다.
#

def solution(N, number):
    if N == number:
        return 1

    # 중간 결과를 저장할 dp 리스트
    dp = [set() for _ in range(8)]
    dp[0].add(N)  # N 자체를 사용하여 만들 수 있는 숫자 저장

    for i in range(1, 8):
        dp[i].add(int(str(N) * (i + 1)))  # N을 i+1번 반복하여 만들 수 있는 숫자 저장

        for j in range(i):
            for op1 in dp[j]:  # dp[j]에서 숫자 하나를 가져옴
                for op2 in dp[i - j - 1]:  # dp[i-j-1]에서 숫자 하나를 가져옴
                    dp[i].add(op1 + op2)  # 덧셈 연산
                    dp[i].add(op1 - op2)  # 뺄셈 연산
                    dp[i].add(op1 * op2)  # 곱셈 연산

                    if op2 != 0:
                        dp[i].add(op1 // op2)  # 나눗셈 연산 (0으로 나누는 경우 제외)

        if number in dp[i]:  # number가 dp[i]에 포함되어 있는 경우
            return i + 1

    return -1  # 최소 사용 횟수가 8을 넘는 경우 -1 반환



# 예제 입력값으로 출력 확인
N = 5
number = 12

print(solution(N, number))  # 예상 출력: 4
