#0512 프로그래머스 해시

#폰켓몬
def solution(nums):
    sol = 0

    get_mon = int(len(nums)/2)
    set_mon = len(set(nums)) #중복을 제외한 배열 - set

    if get_mon < set_mon :
        sol = get_mon
    else :
        sol = set_mon
    return sol



#완주..어쩌구
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion) 
    #Counter -> Key가 이름이고 Value가 count인 딕셔너리 만들어줌
    #Counter class는 상호간의 뺄셈연산을 지원 !!!
    return list(answer.keys())[0]

#answer.keys() -> dict_keys(['leo'])
#list(answer.keys()) -> ['leo']
#list(answer.keys())[0] => leo



#전화번호 목록
def solution(phone_book):
    hash_phone = {}
    for phone in phone_book:
        hash_phone[phone] = 1
        
    for phone in phone_book:
        doo = ''
        for num in phone:
            doo+=num
            if doo in hash_phone and doo!=phone:
                return False
    
    return True



#의상
def solution(clothes):
    
    hash_map = {}
    for clo, clo_type in clothes:
        hash_map[clo_type] = hash_map.get(clo_type, 0) + 1 #Key에 해당하는 Value가 있으면 가져오고 아니면 0을 Default
        
        answer = 1
        for clo_type in hash_map:
            answer *= (hash_map[clo_type] + 1) #입지 않는 경우를 추가해 모든 조합 계산
    
    return answer - 1 #아무것도 입지 않는 경우 제외



#베스트앨범
#못풀겟어요 내일도전..............