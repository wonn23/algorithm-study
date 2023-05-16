#프로그래머스0516 - 황준성
#스택/큐


#---같은 숫자는 싫어---



def solution(arr):
    answer = []
    prev_num = None

    for num in arr:
        if num != prev_num:
            answer.append(num)
        prev_num = num

    return answer



#---다리를 지나는 트럭---



from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    W8OnBridge = 0 # 다리 위 트럭 무게
    waiting = deque(truck_weights) # 대기 트럭 큐
    bridge = deque([0 for _ in range(bridge_length)]) # 다리 길이만큼 0으로 채우기
    
    while len(waiting) or W8OnBridge > 0: # 대기 트럭이 있거나 이동 중인 트럭이 있는 동안 반복
        removedTruck = bridge.popleft() # 다리에서 하나 제거
        W8OnBridge -= removedTruck
        
        if len(waiting) and W8OnBridge + waiting[0] <= weight: # 새 트럭이 다리에 올라갈 수 있으면
            newTruck = waiting.popleft()
            W8OnBridge += newTruck
            
            bridge.append(newTruck)
            
        else:
            bridge.append(0)
            
        time += 1
    return time



#---주식가격---



def solution(prices):
    n = len(prices)
    answer = [0] * n

    for i in range(n - 1):
        for j in range(i + 1, n):
            if prices[j] < prices[i]:
                answer[i] += 1
                break
            else:
                answer[i] += 1

    return answer


from collections import deque # for문으로 풀이했어서 큐로 풀이한 예시를 가져왔다 
def solution(prices):       # 코드를 해석해보자면 prices를 큐로 만들고
    answer = []             # 첫번째 원소를 popleft()로 제거하고 남은 prices와 가격비교
    prices = deque(prices)  # 더 작은 가격을 찾으면 탈출
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer
