####### 같은 숫자는 실허
def solution(arr):
    answer = []
    for i in range(len(arr)):
        answer.append(arr[i])
        if len(answer) > 1:
            if answer[-2] == arr[i]:
                answer.pop(-1)
            else:
                pass
    return answer



###### 올바른 괄호
def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return False
            else:
                left = stack.pop(-1)
                if (i == ")" and left != "("):
                    return False
    if len(stack) == 0:
        return True
    else:
        return False
    
    
    
################ 기능개발
def solution(progresses, speeds):
    answer= []
    queue = []
    
    for i in range(len(progresses)):
        remain_progress = 100 - progresses[i]
        if remain_progress % speeds[i] == 0:
            remain_days = remain_progress // speeds[i]
        else:
            remain_days = remain_progress // speeds[i] + 1
        queue.append(remain_days)
            
    max = -1
    while(len(queue)>0):
        now = queue.pop(0)
        if max < now:
            answer.append(1)
            max = now
        else:
            answer[-1] += 1
        
                
    return(answer)





############### 프로세스
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    print(queue)  # [(0, 2), (1, 1), (2, 3), (3, 2)]
    while True:
        cur = queue.pop(0)
        print(cur)   # (0,2)
        for q in queue:
            if cur[1] < q[1]:   # 방금 꺼낸 프로세스의 우선순위 , q[1] : 대기 중인 것 중 우선순위가 더 높은 프로세스의 우선순위
                queue.append(cur)   # cur: 방금 꺼낸 프로세스  (방금 꺼낸 프로세스를 다시 집어넣기)
                break
        else:    # 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다. (결국 대기 중에서 가장 우선순위 높은 튜)
            answer += 1
            if cur[0] == location:
                return answer


############ 다리를 지나는 트럭

# 1
def solution(bridge_length, weight, truck_weights):
    time = 0    # 최초 경과 시간 (0으로 설정)
    bridge = [0] * bridge_length
    
    currentWeight = 0    # 현재 다리 위의 무게를 저장하는 변수
    while len(truck_weights) > 0:   # truck_weights가 []이 아닐 때까지 반복
        time+=1
        currentWeight = currentWeight - bridge.pop(0)
        
        # print(f"currentWeight: {currentWeight}, truck_weights: {truck_weights}")
        
        if currentWeight + truck_weights[0] <= weight:
            currentWeight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else: 
            bridge.append(0)
        
        # print(bridge)
        
    time += bridge_length
    return(time) 


# 2
from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    time = 0
    bridge = deque([0] * bridge_length)  # [0]*bridge_length 을 덱으로 변환
    truck_weights = deque(truck_weights) # 리스트를 덱으로 변환
    
    currentWeight = 0
    while len(truck_weights) > 0:
        time = time + 1

        currentWeight = currentWeight - bridge.popleft()

        if currentWeight + truck_weights[0] <= weight:
            currentWeight = currentWeight + truck_weights[0]
            bridge.append(truck_weights.popleft())

        else: 
            bridge.append(0)
            
    time = time + bridge_length
    
    return time