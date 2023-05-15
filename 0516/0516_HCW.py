# 같은 숫자는 싫어
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
    
    return answer

# 올바른 괄호

def solution(s):
    answer = 0
    for i in s:
        if answer < 0:
            return False
        elif i == "(" and answer >= 0:
            answer += 1
        elif i == ")" and answer >= 0:
            answer -= 1
        
    if answer == 0:
        return True
    else:
        return False
        
# 기능 개발
import math
def solution(progresses, speeds):
    answer = []
    date = []
    for i in range(len(progresses)):
        date.append(math.ceil((100-progresses[i])/speeds[i]))
    
    count = 0
    max_date = date[0]
    for i in range(len(date)):
        if max_date >= date[i]:
            count += 1
        elif max_date < date[i]:
            answer.append(count)
            max_date = date[i]
            count = 1
    answer.append(count)
    return answer

# 프로세스

# 다리를 지나는 트럭

# 주식가격