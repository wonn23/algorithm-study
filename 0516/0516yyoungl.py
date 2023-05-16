##0516 스터디


### 같은 숫자는 싫어

def solution(arr):
    answer = []
    
    saveNum = -1
    for item in arr:
        if saveNum != item:
            saveNum = item
            answer.append(item)
    
    return answer

### 올바른 괄호
def solution(s):
    answer = True
    
    stack = []
    for x in s:
        if x == "(":
            stack.append(x)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False

    return True


### 기능개발
def solution(progresses, speeds):
    answer = []
    day = 0
    count = 0 
    while progresses:
        if progresses[0] + day*speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count+=1
        else: 
            if count > 0:
                answer.append(count)
                count = 0
            day += 1
        
    answer.append(count)
    
    return answer