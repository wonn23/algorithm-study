#####[미션1] 계단 오르기######
# 60점밖에 안 돼여

def stair(data):
    # 리스트의 길이를 n에 저장합니다.
    n = len(data)
    
    if n == 1:
        # 계단이 1개일 때의 점수를 반환해 주세요.
        return 10
    if n == 2:
        # 계단이 2개일 때의 점수를 반환해 주세요.
        return 30
    if n == 3:
        # 계단이 3개일 때의 점수를 반환해 주세요.
        return 25
        
    # 기억해야 하는 정보들은 길이 n 짜리 Table에 저장할 예정이에요.
    # Table의 모든 원소의 초기값은 0으로 설정돼요.
    Table = [0 for i in range(n)]
    print(Table)
    
    # 첫 번째 계단에서의 점수를 저장해 주세요.
    Table[0] = data[0]
    # 두 번째 계단에서의 점수를 저장해 주세요.
    Table[1] = data[1]
    # 세 번째 계단에서의 점수를 저장해 주세요.
    Table[2] = max(data[0]+data[2],data[1]+data[2])
    # Table[2] = data[0]+data[2]
    print(Table)
    for i in range(3, n):
        # i 번째 계단에서의 점수를 저장해 주세요.
        Table[i] = max(Table[i-3] + data[i-1] + data[i], Table[i-2]+data[i])
    # 점수의 최댓값을 반환해 주세요.
    print(Table)
    return Table[i]


def main():
    data = [int(x) for x in input().split()]
    print(stair(data))


if __name__ == "__main__":
    main()








#####[미션2] 짜장,짬뽕,볶음밥######
# 내가 이해하려고 만든 PPT 공유할게여

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
    # print(Table,"  ",data)
    for i in range(1, n):
        for j in range(3):
            # i일 차 j번째 음식을 선택하지 않았을 때의 최적 선호도를 계산
            # 이전 날짜까지의 최적 선호도를 이용
            max_val = max(Table[i-1][(j+1)%3], Table[i-1][(j+2)%3])

            # i일 차 j번째 음식을 선택했을 때의 최적 선호도를 계산
            # 이전 날짜까지의 최적 선호도와 i일 차 j번째 음식의 선호도를 더하기
            cur_val = max_val + data[i][j]

            # Table[i][j]에 계산한 최적 선호도를 저장합니다.
            Table[i][j] = cur_val

    # 마지막 날짜의 최적 선호도를 반환합니다.
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










#####[미션3] 블록 채우기######
#이거 이해 잘 안 가서 은석님꺼 베끼기 스킬~
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
        
        Table[i] = (Table[i-1] + Table[i-2]) % 1000000007
    
    # 상자의 크기가 2 * n일때, 블록으로 채울 수 있는 경우의 수를 반환해 주세요.
    return Table[i]


def main():
    n = int(input())
    print(fillBox(n))


if __name__ == "__main__":
    main()










#####[미션4] 줄 세우기######
# 이것두 피피티 만들엇슴니돠

import sys

def lining(n):
    # 테이블을 알맞은 길이로 초기화 해주세요.
    Table = [0 for i in range(n + 1)]
    
    # 테이블의 초깃값을 올바르게 저장해 주세요.
    Table[1] = 2
    Table[2] = 3
    
    for i in range(3, n + 1):
        # 이전 데이터를 효과적으로 활용해 테이블을 완성해 주세요.
        # 테이블에 넣을 데이터는 반드시 1000000007로 나눈 나머지를 저장해 주세요.
        Table[i] = (Table[i-2] + Table[i-1])%1000000007
    
    # n명의 학생을 줄 세우는 경우의 수를 반환해 주세요.
    return Table[i]


def main():
    data = int(input())
    print(lining(data))


if __name__ == "__main__":
    main()








#####[미션5] 숫자 만들기######
#이것도 이해 잘 안 가서 은석님꺼 베끼기 스킬~S2 

def makeNumber(n, m):
    Table = [0] * (n+1)
    Table[0] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if j <= i:
                Table[i] += Table[i-j]
                Table[i] = Table[i] % 1000000007
    
    return Table[n]



def main():
    n, m = (int(x) for x in input().split())
    print(makeNumber(n, m))


if __name__ == "__main__":
    main()


