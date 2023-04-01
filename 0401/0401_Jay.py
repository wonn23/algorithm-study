##### 1.최대공통부분문자열
def maxCommonSequence(s1, s2):
    n = len(s1)
    m = len(s2)
    
    # 2차원 리스트를 활용해 최대 공통부분의 길이를 저장해 봅시다.
    # 초깃값으로는 0을 설정해주면 돼요.
    Table = [[0] * (m+1) for _ in range(n+1)]
    
    # s1[0]과 s2[0]이 같으면 1을 다르면 0을 저장하세요.
    Table[0][0] = 1 if s1[0] == s2[0] else 0
    
    for i in range(1, m):
        # Table의 첫 번째 행에 올바른 값을 설정해 주세요.
        Table[0][i] = 1 if s1[0] == s2[i] or Table[0][0] == 1 else 0
    
    for i in range(1, n):
        # Table의 첫 번째 열에 올바른 값을 설정해 주세요.
        Table[i][0] = 1 if s1[i] == s2[0] or Table[0][0] == 1 else 0
    
    
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

################## 2번 숫자 삼각형

def maxTriangle(triangle) :
    n = len(triangle)
    
# 2차원 리스트를 활용해 Table을 초기화 해주세요.
    Table = [[0] * i for i in range(1, n+1)]

# 숫자 삼각형의 맨 첫 번째 숫자를 테이블에 입력해 봅시다. 
    Table[0][0] = triangle[0][0]

# Table을 갱신해 주세요.
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                Table[i][j] = Table[i-1][j] + triangle[i][j]
            elif j == i:
                Table[i][j] = Table[i-1][j-1] + triangle[i][j]
            else:
                Table[i][j] = max(Table[i-1][j-1], Table[i-1][j]) + triangle[i][j]

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

################ 3번 두 문자열 사이의 거리

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
    arr = LCS(s1,s2)
    
    return len(s1) + len(s2) - (2 * arr) # 공통인부분이 겹치니까 2배해서 빼줘야됨.


def main():
    s1 = input()
    s2 = input()

    print(strDistance(s1, s2))


if __name__ == "__main__":
    main()


############################ 4번 펠린드롬 만들기


def palindrome(data):
    n = len(data)

    # 이전 작은 문제의 해답을 2차원 리스트 Table에 저장할 예정입니다.
    # Table을 알맞게 초기화해주세요.
    Table = [[0] * n for _ in range(n)]
    
    # Table을 갱신해 주세요.
    
    for i in range(n): # 문자열 하나
        Table[i][i] = 0

    for i in range(n-1): # 문자열 두개
        if data[i] == data[i+1]:
            Table[i][i+1] = 0
        else:
            Table[i][i+1] = 1

    for k in range(2, n): # 문자열 3개 이상
        for i in range(n-k):
            j = i+k
            if data[i] == data[j]:
                Table[i][j] = Table[i+1][j-1]
            else:
                Table[i][j] = min(Table[i+1][j], Table[i][j-1]) + 1

    # 올바른 결과를 반환해주세요.
    return Table[0][n-1]


def main():
    s = input()

    print(palindrome(s))


if __name__ == "__main__":
    main()
