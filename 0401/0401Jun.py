#동적 계획법 심화 - 황준성



#---미션2 - 숫자 삼각형---



def maxTriangle(triangle) :
    n = len(triangle)
    
    # 2차원 리스트를 활용해 Table을 초기화 해주세요.
    Table = [[0 for j in range(i + 1)]for i in range(n)]
    
    # 숫자 삼각형의 맨 첫 번째 숫자를 테이블에 입력해 봅시다. 
    Table[0][0] = triangle[0][0]
    
    # Table을 갱신해 주세요.
    for i in range(1, n):
        for j in range(i + 1):
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