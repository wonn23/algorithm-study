### 폰켓몬

def solution(nums):
    N = len(nums)
    get = []
    for i in range(N):
        if nums[i] not in get and len(get) < N//2:
            get.append(nums[i])
    return len(get)


### 완주하지 못한 선수

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
            break
    else:
        return participant[-1]
    

    ### 전화번호 목록

    def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False;
            break
    return answer