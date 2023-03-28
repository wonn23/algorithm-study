#동적 계획법 기초 - 황준성



#---미션1 - 계단 오르기---
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
        return max(data[0] + data[2], data[1] + data[2])
        
    # 기억해야 하는 정보들은 길이 n 짜리 Table에 저장할 예정이에요.
    # Table의 모든 원소의 초기값은 0으로 설정돼요.
    Table = [0 for i in range(n)]
    
    # 첫 번째 계단에서의 점수를 저장해 주세요.
    Table[0] = data[0]
    # 두 번째 계단에서의 점수를 저장해 주세요.
    Table[1] = data[0] + data[1]
    # 세 번째 계단에서의 점수를 저장해 주세요.
    Table[2] = max(data[0] + data[2], data[1] + data[2])
    
    for i in range(3, n):
        # i 번째 계단에서의 점수를 저장해 주세요.
        Table[i] = max(Table[i-3] + data[i-1] + data[i], Table[i-2] + data[i])
    
    # 점수의 최댓값을 반환해 주세요.
    return Table[n - 1]


def main():
    data = [int(x) for x in input().split()]
    print(stair(data))


if __name__ == "__main__":
    main()



#---미션2 - 짜장, 짬뽕, 볶음밥---



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
        Table[i][0] = max(Table[i-1][1], Table[i-1][2]) + data[i][0]
        Table[i][1] = max(Table[i-1][0], Table[i-1][2]) + data[i][1]
        Table[i][2] = max(Table[i-1][0], Table[i-1][1]) + data[i][2]
    
    # 음식 선호도의 최댓값을 반환해 주세요.
    return max(Table[n-1])


def main():
    n = int(input())

    data = []

    for i in range(n) :
        __line = [int(x) for x in input().split()]
        data.append(__line)

    print(eating(data))


if __name__ == "__main__":
    main()



#---미션3 - 블록 채우기---



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
        Table[i] = (Table[i - 1] + Table[i - 2]) % 1000000007
    
    # 상자의 크기가 2 * n일때, 블록으로 채울 수 있는 경우의 수를 반환해 주세요.
    return Table[n]


def main():
    n = int(input())
    print(fillBox(n))


if __name__ == "__main__":
    main()



#---미션4 - 줄 세우기---



import sys

def lining(n):
    # 테이블을 알맞은 길이로 초기화 해주세요.
    Table = [0] * (n + 1)
    
    # 테이블의 초깃값을 올바르게 저장해 주세요.
    Table[1] = 2
    Table[2] = 3
    
    for i in range(3, n + 1):
        # 이전 데이터를 효과적으로 활용해 테이블을 완성해 주세요.
        # 테이블에 넣을 데이터는 반드시 1000000007로 나눈 나머지를 저장해 주세요.
        Table[i] = (Table[i - 1] + Table[i - 2]) % 1000000007
    
    # n명의 학생을 줄 세우는 경우의 수를 반환해 주세요.
    return Table[n]


def main():
    data = int(input())
    print(lining(data))


if __name__ == "__main__":
    main()



#---미션5 - 숫자 만들기---



def makeNumber(n, m):
    Table = [0] * (n + 1)
    Table[0] = 1

    for i in range(1, n + 1):
        for j in range(i, m + 1):
            if i >= j:
                Table[i] += Table[i-j]
                Table[i] %= 1000000007
    
    return Table[n]


def main():
    n, m = (int(x) for x in input().split())
    print(makeNumber(n, m))


if __name__ == "__main__":
    main()
