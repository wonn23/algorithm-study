###### 폰켓몬
def solution(nums):
    remove_duplicate = list(set(nums))
    if len(nums)/2 > len(remove_duplicate):
        return len(remove_duplicate)
    elif len(nums)/2 < len(remove_duplicate):
        return len(nums) / 2
    else:
        return len(nums) / 2  # len(remove_duplicate)도 가능
    
    
##### 완주하지 못한 선수
# 코드 실행은 통과, 제출은 안통과
def solution(participant, completion):
    answer = ''
    hash = {}
    
    for name in completion:
        hash[name] = 1
        
    for name in participant:
        if name in hash:
            del hash[name]
        else:
            answer += name
    
    return answer


####### 의상
def solution(clothes):
    answer = 1
    hash = {}
    
    for Name, Type in clothes:
        if Type not in hash:
            hash[Type] = [Name]
        else:
            hash[Type].append(Name)
    # print(hash)
    
    for i in range(len(hash)):
        key_list = list(hash.keys())
        value_list = hash[key_list[i]]
        answer = answer * (len(value_list) + 1)
        
    return answer - 1