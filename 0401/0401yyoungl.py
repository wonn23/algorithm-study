## 0401 동적계획법 심화
#미션1 최대 공통부분 문자열

def maxCommonSequence(s1, s2):
    n = len(s1)
    m = len(s2)
    
    # 2차원 리스트를 활용해 최대 공통부분의 길이를 저장해 봅시다.
    # 초깃값으로는 0을 설정해주면 돼요.
    Table = [[0 for _ in range(m)] for _ in range(n)] #s1, s2
    #print(Table)
    # s1[0]과 s2[0]이 같으면 1을 다르면 0을 저장하세요.
    if s1[0] == s2[0]:
        Table[0][0] = 1
    
    for i in range(1, n):
        # Table의 첫 번째 열에 올바른 값을 설정해 주세요.
        if s1[i] == s2[0]: 
            Table[i][0] = 1
        else:
            Table[i][0] = Table[i-1][0]
    
    for i in range(1, m):
        # Table의 첫 번째 행에 올바른 값을 설정해 주세요.
        if s2[i] == s1[0]: 
            Table[0][i] = 1
        else:
            Table[0][i] = Table[0][i-1]
    
    
    # Table을 갱신해 주세요.
    for i in range(1, n):
        for j in range(1, m):
            if s1[i] == s2[j]:
                Table[i][j] = Table[i-1][j-1] + 1
            else:
                Table[i][j] = max(Table[i-1][j], Table[i][j-1])
    
    # 올바른 결과를 반환해 주세요.
    return Table[n-1][m-1]


def main():
    s1 = input()
    s2 = input()

    print(maxCommonSequence(s1, s2))


if __name__ == "__main__":
    main()



#미션2 숫자 삼각형

def maxTriangle(triangle) :
    n = len(triangle)
    #print(triangle)
    # 2차원 리스트를 활용해 Table을 초기화 해주세요.
    Table = [[0 for i in range(n)] for j in range(n)]
    
    # 숫자 삼각형의 맨 첫 번째 숫자를 테이블에 입력해 봅시다. 
    Table [0][0] = triangle[0][0]
    
    # Table을 갱신해 주세요.
    for i in range(1, n): # 1 ~ n-1
        for j in range(i+1): # 0 ~ i 
            if j==0:
                Table[i][j] = Table[i-1][j] + triangle[i][j]
            elif j==i: #오른쪽 끝열
                Table[i][j] = Table[i-1][j-1] + triangle[i][j]
            else:
                Table[i][j] = max(Table[i-1][j-1], Table[i-1][j]) + triangle[i][j]

    # print(Table[n-1])


    # Table로부터 알맞은 결과를 반환해 주세요.
    return max(Table[n-1])


def main():
    n = int(input())
    triangle = []

    for i in range(n) :
        triangle.append([int(v) for v in input().split()])

    print(maxTriangle(triangle))


if __name__ == "__main__":
    main()


#미션3 두 문자열 사이의 거리


# 앞에서 함께 풀어봤던 최대 공통부분 문자열 함수예요.
# 이 함수를 유용하게 활용한다면 strDistance() 함수를 손쉽게 완성할 수 있답니다!
def LCS(s1, s2) :
    n = len(s1)
    m = len(s2)
    
    Table = [ [ 0 for i in range(m) ] for j in range(n) ]
    
    Table[0][0] = 1 if s1[0] == s2[0] else 0
    
    for i in range(1, m) :
        Table[0][i] = Table[0][i-1] if s1[0] != s2[i] else 1
    
    for i in range(1, n) :
        Table[i][0] = Table[i-1][0] if s1[i] != s2[0] else 1
    
    for i in range(1, n) :
        for j in range(1, m) :
            if s1[i] == s2[j] :
                Table[i][j] = Table[i-1][j-1] + 1
            else :
                Table[i][j] = max(Table[i-1][j], Table[i][j-1])
    
    return Table[n-1][m-1]


# 문자열 s1, s2사이의 거리를 계산하는 함수예요.
def strDistance(s1, s2):
    return len(s1) + len(s2) - 2 * LCS(s1, s2) # 공통 부분에서 다른 부분 찾기 > 길이 + 길이 하면 공통부분 겹치니까 2 * 공통 으로 빼주기


def main():
    s1 = input()
    s2 = input()

    print(strDistance(s1, s2))


if __name__ == "__main__":
    main()



#미션4 회문 만들기

def palindrome(data) :
    n = len(data)
    
    # 이전 작은 문제의 해답을 2차원 리스트 Table에 저장할 예정이랍니다.
    # Table을 알맞게 초기화 해주세요.
    Table = [[0 for _ in range(n)] for _ in range(n)]
    
    # Table을 갱신해 주세요.
    Table[0][0] = 0

    for i in range(n-1,-1,-1):
         for j in range(i+1,n):
            if data[i] == data[j]:
                Table[i][j] = Table[i+1][j-1]
            else:
                Table[i][j] = min(Table[i+1][j],Table[i][j-1])+1

    
    # 올바른 결과를 반환해 주세요.
    return Table[0][n-1]


def main():
    s = input()

    print(palindrome(s))


if __name__ == "__main__":
    main()
