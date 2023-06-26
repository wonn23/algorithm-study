# 탐욕법 > 체육복


def solution(n, lost, reserve):
    answer = n - len(lost)
    new_lost = []
    lost.sort()
    reserve.sort()
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            answer += 1
        else:
            new_lost.append(i)
            lost = new_lost
    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
            answer += 1
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            answer += 1
    return answer


# 탐욕법 > 조이스틱
def solution(name):
    # ord()를 활용하면 아래와 같은 숫자가 나온다.
    # dict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,
    #           'N':13, 'O':12,'P':11,'Q':10,'R':9,'S':8,'T':7,'U':6,'V':5,'W':4,'X':3,'Y':2,'Z':1}

    # ord()란 아스키코드의 숫자를 말한다.
    # ord('A') = 65, ord('B') = 66, ... , ord('Z') = 90
    def solution(name):
        answer = 0
        # 상하로 움직인 수 모두 더하기
        num_list = [min(ord(i) - ord("A"), ord("Z") - ord(n) + 1) for i in name]
        answer += sum(num_list)

        min_move = len(name) - 1
        # "JEROEN"
        for i, c in enumerate(name):  # (0,'J'), (1,'E'), ...
            next_i = i + 1

            while next_i < len(name) and name[next_i] == "A":
                next_i += 1
            # 각 문자부터 'A..'문자가 있을경우 몇번씩 조이스틱쓰는지 체크
            min_move = min(
                min_move, 2 * i + len(name) - next_i, 2 * (len(name) - next_i) + i
            )

        return answer + min_move


# 탐욕법 > 큰 수 만들기


def solution(number, k):
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    if k != 0:  # "1111111" 이고 k=2 이면 while문에 못들어가고 계속 stack에 쌓인다.
        stack = stack[:-k]
    return "".join(stack)


# 탐욕법 > 구명보트

# 탐욕법 > 섬 연결하기

# 탐욕법 > 단속 카메라
