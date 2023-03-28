############################# 1번

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
        Table[i] = max(Table[i-3] + data[i-1] + data[i], Table[i-2]+data[i])
    
    # 점수의 최댓값을 반환해 주세요.
    return Table[i]


def main():
    data = [int(x) for x in input().split()]
    print(stair(data))


if __name__ == "__main__":
    main()

############################# 2번

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
        Table[i][0] = data[i][0] + max(Table[i-1][1], Table[i-1][2])
        Table[i][1] = data[i][1] + max(Table[i-1][0], Table[i-1][2])
        Table[i][2] = data[i][2] + max(Table[i-1][0], Table[i-1][1])
    
    # 음식 선호도의 최댓값을 반환해 주세요.
    return max(Table[-1])


def main():
    n = int(input())

    data = []

    for i in range(n) :
        __line = [int(x) for x in input().split()]
        data.append(__line)

    print(eating(data))
    # print(data)


if __name__ == "__main__":
    main()

################################## 3번

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

########################################## 4번

def lining(n):
    Table = [0] * (n+1)
    
    # 초기값 설정
    Table[1] = 2 # p/q
    Table[2] = 3 # qq / qp / pq
    
    for i in range(3, n+1):
        Table[i] = (Table[i-1] + Table[i-2]) % 1000000007
    
    return Table[n] % 1000000007


def main():
    data = int(input())
    print(lining(data))


if __name__ == "__main__":
    main()

######################################### 5번

def makeNumber(n, m):
    # 1부터 m 사이의 수를 뽑아서 합한 값이 n이 되는 경우의 수를 계산합니다.
    # 1부터 m까지의 수를 더하여 n을 만드는 경우의 수를 1,000,000,007로? 나눈 나머지를 출력...
    # Table을 n+1 크기로 만들고, 모든 원소를 0으로 초기화해보자... 
    Table = [0] * (n+1)
    Table[0] = 1 #아무것도 없을때(0) 경우의 수를 하나로 치기위해 만들어줌

    for i in range(1, n+1):
        for j in range(1, m+1):
            if j <= i:
                Table[i] += Table[i-j]
                Table[i] %= 1000000007

    # Table[n]을 반환합니다.
    return Table[i]

def main():
    n, m = map(int, input().split())
    print(makeNumber(n, m))

if __name__ == "__main__":
    main()
