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

# 탐욕법 > 큰 수 만들기

# 탐욕법 > 구명보트

# 탐욕법 > 섬 연결하기

# 탐욕법 > 단속 카메라
