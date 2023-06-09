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

from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    wait_truck = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    bridge_weight = 0
    
    while len(bridge):
        answer += 1
        bridge_weight -= bridge[0] # 차량 뽑아내기 전 다리 무게 계산하기
        bridge.popleft() # 다리 위에 있는 차량을 뽑아내기
        if wait_truck:
            if bridge_weight + wait_truck[0] <= weight: # 차량이 다리 위에 올라갈 수 있는지 확인하기 
                truck = wait_truck.popleft() # 대기 중인 트럭 한대 뽑아내기
                bridge_weight += truck # 트럭 무게 다리에 더해주기
                bridge.append(truck) # 다리에 트럭 올림
            else:
                bridge.append(0)
    return answer

# 주식가격