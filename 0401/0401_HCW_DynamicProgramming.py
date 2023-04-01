### 미션1 - 최대 공통부분 문자열 ###

def maxCommonSequence(s1, s2):
    n = len(s1)
    m = len(s2)
    
    # 2차원 리스트를 활용해 최대 공통부분의 길이를 저장해 봅시다.
    # 초깃값으로는 0을 설정해주면 돼요.
    Table = [[ 0 for _ in range(n)] for _ in range(m)] # n은 가로, m은 세로
    

    # s1[0]과 s2[0]이 같으면 1을 다르면 0을 저장하세요.
    if s1[0] == s2[0]:
        Table[0][0] = 1 # 기본적으로 0으로 초기화 되어있음

    
    for i in range(1, m):
        # Table의 첫 번째 행에 올바른 값을 설정해 주세요.
        if s1[0] == s2[i]:
            Table[0][i]=1
    
    for i in range(1, n):
        # Table의 첫 번째 열에 올바른 값을 설정해 주세요.
        if s2[0] == s1[i]:
            Table[i][0] = 1
        
    # Table을 갱신해 주세요.
    max_len = 0
    for i in range(1,n):
        for j in range(1,m):
            if s1[i] == s2[j]:
                Table[i][j] = max_len+1
                Table[i][j] = max(Table[i][j], max_len)
    # 올바른 결과를 반환해 주세요.
    return max(Table[n-1][m-1],max_len)


def main():
    s1 = input()
    s2 = input()

    print(maxCommonSequence(s1, s2))


if __name__ == "__main__":
    main()
