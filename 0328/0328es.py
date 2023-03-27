#0328 동적 계획법 은석

############
#1 계단오르기
def stair(data):
    # 리스트의 길이를 n에 저장합니다.
    n = len(data)
    
    if n == 1:
        # 계단이 1개일 때의 점수를 반환해 주세요.
        return data[0]
    if n == 2:
        # 계단이 2개일 때의 점수를 반환해 주세요.
        return data[0]+data[1]
    if n == 3:
        # 계단이 3개일 때의 점수를 반환해 주세요.
        return data[0]+data[2]
        
    # 기억해야 하는 정보들은 길이 n 짜리 Table에 저장할 예정이에요.
    # Table의 모든 원소의 초기값은 0으로 설정돼요.
    Table = [0 for i in range(n)]
    
    # 첫 번째 계단에서의 점수를 저장해 주세요.
    Table[0] = data[0]
    # 두 번째 계단에서의 점수를 저장해 주세요.
    Table[1] = data[0]+data[1]
    # 세 번째 계단에서의 점수를 저장해 주세요.
    Table[2] = data[0]+data[2]
    
    for i in range(3, n):
        # i 번째 계단에서의 점수를 저장해 주세요.
        Table[i] = max(Table[i-3] + data[i-1] + data[i], Table[i-2]+data[i])
    
    # 점수의 최댓값을 반환해 주세요.
    return Table[i]


def main():
    data = [int(x) for x in input().split()]
    print(stair(data))


if __name__ == "__main__":
    main()


#2 짜장, 짬뽕, 볶음밥 (40점)
###상훈이 이자식아......###### 
import sys

def eating(data):
    # 선호도 리스트의 길이를 n에 저장해요.
    n = len(data)

    # Table에는 상훈이의 날짜별 최적 선호도를 저장해요.
    #   [예시]
    #     Table = [[1일 차 최적 선호도 초깃값(짜장, 짬뽕, 볶음밥 순서)], [2일 차 최적 선호도 초깃값(짜장, 짬뽕, 볶음밥 순서)], ...]
    # 초깃값은 모두 0으로 초기화 해요.
    Table = [[0 for i in range(3)] for j in range(n)]
    Meal = []
    # 1일 차 음식 선호도를 Table에 저장해 주세요.
    Table[0][0] = data[0][0]
    Table[0][1] = data[0][1]
    Table[0][2] = data[0][2]

    Meal.append(max(Table[0]))
    
    
    for i in range(1, n):
        # i일 차 음식 선호도를 Table에 저장해 주세요.
        Table[i][0] = data[i][0]
        Table[i][1] = data[i][1]
        Table[i][2] = data[i][2]

        mealIndex = Table[i-1].index(Meal[i-1])
        
        popped = Table[i].pop(Table[i-1].index(Meal[i-1]))
        

        Meal.append(max(Table[i]))
        Table[i].insert(mealIndex,popped)
        #print(Meal)
        #print(Table)

        
    # 음식 선호도의 최댓값을 반환해 주세요. 
    return sum(Meal)

def main():
    n = int(input())

    data = []

    for i in range(n) :
        __line = [int(x) for x in input().split()]
        data.append(__line)

    print(eating(data))


if __name__ == "__main__":
    main()


##############
#3 블록 채우기
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
        #가로 : 2
        #세로 : n
        Table[i] = (Table[i-1] + Table[i-2]) % 1000000007
    
    # 상자의 크기가 2 * n일때, 블록으로 채울 수 있는 경우의 수를 반환해 주세요.
    return Table[n]


def main():
    n = int(input())
    print(fillBox(n))


if __name__ == "__main__":
    main()


############
#4 줄 세우기
import sys

def lining(n):
    # 테이블을 알맞은 길이로 초기화 해주세요.
    Table = [0] * (n+1)
    
    # 테이블의 초깃값을 올바르게 저장해 주세요.
    Table[1] = 2
    Table[2] = 3
    
    for i in range(3, n + 1):
        # 이전 데이터를 효과적으로 활용해 테이블을 완성해 주세요.
        # 테이블에 넣을 데이터는 반드시 1000000007로 나눈 나머지를 저장해 주세요.
        Table[i] = (Table[i-1] + Table[i-2]) % 1000000007
    
    # n명의 학생을 줄 세우는 경우의 수를 반환해 주세요.
    return Table[n]


def main():
    data = int(input())
    print(lining(data))


if __name__ == "__main__":
    main()


#############
#5 숫자 만들기
def makeNumber(n, m):
    #1부터 m 사이의 수를 뽑아서 합한 값이 n이 되는 경우
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