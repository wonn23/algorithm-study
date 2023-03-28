#### 0328 스터디
#### 미션1 계단 오르기
def stair(data):
    # 리스트의 길이를 n에 저장합니다.
    n = len(data)
    
    if n == 1:
        # 계단이 1개일 때의 점수를 반환해 주세요.
        return data[0]
    if n == 2:
        # 계단이 2개일 때의 점수를 반환해 주세요.
        return data[0] + data[1]
    if n == 3:
        # 계단이 3개일 때의 점수를 반환해 주세요.
        return data[0] + data[2]
        
    # 기억해야 하는 정보들은 길이 n 짜리 Table에 저장할 예정이에요.
    # Table의 모든 원소의 초기값은 0으로 설정돼요.
    Table = [0 for i in range(n)]
    
    # 첫 번째 계단에서의 점수를 저장해 주세요.
    Table[0] = data[0]
    # 두 번째 계단에서의 점수를 저장해 주세요.
    Table[1] = data[0] + data[1]
    # 세 번째 계단에서의 점수를 저장해 주세요.
    Table[2] = data[0] + data[2]
    
    for i in range(3, n):
        # i 번째 계단에서의 점수를 저장해 주세요.
        # i 번째 계단을 밟기 위해서는 i-1 번째를 밟는 경우 / i-2 번째를 밟는 경우 두 가지가 있음
        # 이때 i-1 번째 계단을 밟으려면 무조건 두 계단 아래인 i-3 번째 계단을 밟아야 하므로 ... i-3 까지 왔을 때 받을 수 있는 최대 점수를 이미 알고 있음~ 그리고 i-2도 마찬가지! 
        Table[i] = max(Table[i-3] + data[i-1] + data[i], Table[i-2] + data[i])
    
    # 점수의 최댓값을 반환해 주세요.
    return Table[i]


def main():
    data = [int(x) for x in input().split()]
    print(stair(data))


if __name__ == "__main__":
    main()



#### 미션2 짜장, 짬뽕, 볶음밥
import sys

def eating(data):
    # 선호도 리스트의 길이를 n에 저장해요.
    n = len(data)

    # Table에는 상훈이의 날짜별 최적 선호도를 저장해요.
    #   [예시]
    #     Table = [[1일 차 최적 선호도 초깃값(짜장, 짬뽕, 볶음밥 순서)], [2일 차 최적 선호도 초깃값(짜장, 짬뽕, 볶음밥 순서)], ...]
    # 초깃값은 모두 0으로 초기화 해요.
    Table = [[0 for i in range(3)] for j in range(n)]

    # 1일 차 음식 선호도를 Table에 저장해 주세요.
    Table[0][0] = data[0][0]
    Table[0][1] = data[0][1]
    Table[0][2] = data[0][2]

    for i in range(1, n):
        # i일 차 음식 선호도를 Table에 저장해 주세요.
        Table[i][0] = data[i][0]
        Table[i][1] = data[i][1]
        Table[i][2] = data[i][2]
    
    # 음식 선호도의 최댓값을 반환해 주세요.
    return 0


def main():
    n = int(input())

    data = []

    for i in range(n) :
        __line = [int(x) for x in input().split()]
        data.append(__line)

    print(eating(data))


if __name__ == "__main__":
    main()



#### 미션3 블록 채우기
def fillBox(n):
    if n == 1:
        # 상자의 크기가 2 * 1일때, 블록으로 채울 수 있는 경우의 수를 반환해 주세요.
        return 1
    
    if n == 2:
        # 상자의 크기가 2 * 2일때, 블록으로 채울 수 있는 경우의 수를 반환해 주세요.
        return 2
    
    # 상자에 블록을 채우는 경우의 수를 저장할 Table이에요.
    # 모두 0으로 초기화 해요.
    Table = [0 for i in range(n + 1)]
    
    # 상자의 크기가 2 * 1일때, 블록으로 채울 수 있는 경우의 수를 저장해 주세요.
    Table[1] = 1
    # 상자의 크기가 2 * 2일때, 블록으로 채울 수 있는 경우의 수를 저장해 주세요.
    Table[2] = 2
    
    for i in range(3, n + 1):
        # 상자의 크기가 2 * i일때, 블록으로 채울 수 있는 경우의 수를 저장해 주세요.
        # 테이블에 넣을 데이터는 반드시 1000000007로 나눈 나머지를 저장해 주세요.
        Table[i] = Table[i-1] + Table[i-2]
    # 상자의 크기가 2 * n일때, 블록으로 채울 수 있는 경우의 수를 반환해 주세요.
    Table = [i%1000000007 for i in Table]
    return Table[i]


def main():
    n = int(input())
    print(fillBox(n))


if __name__ == "__main__":
    main()



#### 미션4 줄 세우기
import sys

def lining(n):
    # 테이블을 알맞은 길이로 초기화 해주세요.
    Table = [0] * (n+1)
    
    # 테이블의 초깃값을 올바르게 저장해 주세요.
    Table[1] = 2 # 남/여
    Table[2] = 3 # 여여/남여/여남
    # 3명일 경우,
    # 남여남, 여남여/여여남/남여여, 여여여 ==> 1명일 경우 + 2명일 경우... 앞의 경우에 한 개씩 추가한 경우 따라서 5개
    # 4명일 경우,
    # 남여여여 조합 4개 / 남여여남, 남여남여, 여남여남 / 여여여여 === > 5 + 3




    for i in range(3, n + 1):
        # 이전 데이터를 효과적으로 활용해 테이블을 완성해 주세요.
        # 테이블에 넣을 데이터는 반드시 1000000007로 나눈 나머지를 저장해 주세요.
        Table[i] = Table[i-1] + Table[i-2]
        Table = [i % 1000000007 for i in Table]
    # n명의 학생을 줄 세우는 경우의 수를 반환해 주세요.
    return Table[i]


def main():
    data = int(input())
    print(lining(data))


if __name__ == "__main__":
    main()



#### 미션5 숫자 만들기
def makeNumber(n, m):
    cases = [0] * (n+1) #여기에 1을 만드는 경우, 2를 만드는 경우... 를 만들려 한다
    cases[0] = 1


    # 만약 3의 경우,
    # (1, 1, 1) (2, 1) (1, 2) (3) == > cases[1] + cases[2] + 1 = 4
    # 4의 경우
    # (1, 1, 1, 1) (1, 1, 2) (1, 2, 1) (2, 1, 1) (2, 2) (1, 3) (3, 1) (4)
    # ==> C(1) + C(2) + C(3) + 1 이다
    # 지금 보니까 고등수학의 중복조합과 비슷한 것 같기도 하고...
    # https://daily-life-of-bsh.tistory.com/32 여기 봄

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i >= j:
                cases[i] += cases[i-j]
    
    cases = [x%1000000007 for x in cases]

    
    return cases[n]


def main():
    n, m = (int(x) for x in input().split())
    print(makeNumber(n, m))


if __name__ == "__main__":
    main()
