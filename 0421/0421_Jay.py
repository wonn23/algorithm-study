#1018 체스판
N, M = map(int, input().split())  
board = [input() for _ in range(N)]  # 보드 입력 받기

def count_min(board):

    chess1 = ['BWBWBWBW', 'WBWBWBWB'] * 4 #흑으로 시작하는 경우
    chess2 = ['WBWBWBWB', 'BWBWBWBW'] * 4 #백으로 시작하는 경우

    cnt1, cnt2 = 0, 0 #차이값 저장 변수 0 으로 초기화

    for i in range(8):
        for j in range(8):
            if board[i][j] != chess1[i][j]: #비교하면서 다르면 차이값 1씩 올리기
                cnt1 += 1
            if board[i][j] != chess2[i][j]:
                cnt2 += 1
    
    return min(cnt1, cnt2) #둘중 차이값 적은 보드 선택


answer = N * M  # 초기값 설정

for i in range(N - 7):
    for j in range(M - 7):
        chess_board = [board[i+k][j:j+8] for k in range(8)] #리스트 컴프리헨션으로 작성 연습! k는 0~7까지 반복해서 받음
        # 8x8 체스판 슬라이싱을 통해 만들기!  
        # i부터 i+7까지의 행을 슬라이싱한 뒤,각 행에서 j부터 j+7까지의 연속된 열을 슬라이싱한 리스트를 생성한다. 
        # k 변수로 0부터 7까지 반복한다 따라서, board의 i부터 i+7까지의 행을 만들고, 각 행에서 j부터 j+7까지의 연속된 열을 8x8 크기의 체스판 조각을 chess_board 변수에 할당한다.
        temp = count_min(chess_board)  # 현재 체스판에서의 최솟값 계산
        answer = min(answer, temp)  # 현재 값과 최솟값 비교하여 갱신



print(answer)  # 결과 출력

#숌
n = int(input())
count = 0
num = 665

while count < n:
    num += 1
    if '666' in str(num):
        count += 1

print(num)

#퇴사

def get_max_profit(N, schedules):
    dp = [0] * (N + 1)  # DP 테이블 초기화

    for i in range(N - 1, -1, -1):  # 뒤에서부터 역순으로 DP 진행
        next_day = i + schedules[i][0]  # 다음 날짜 계산

        # 퇴사 날짜를 넘어가는 경우, 다음 날짜의 DP 값을 현재 날짜의 DP 값에 복사
        if next_day > N:
            dp[i] = dp[i + 1]
        # 현재 날짜의 상담을 하는 경우, 상담 완료일에 받을 수 있는 금액을 더하여 최댓값을 구함
        else:
            dp[i] = max(dp[i + 1], schedules[i][1] + dp[next_day])

    return dp[0]  # 0번째 날의 DP 값이 최대 이익

# 입력 처리
N = int(input())  # N 입력
schedules = []  # 상담 일정 리스트
for _ in range(N):
    schedules.append(list(map(int, input().split())))  # Ti, Pi 입력

# 최대 이익 계산
max_profit = get_max_profit(N, schedules)

# 결과 출력
print(max_profit)
