#0519 프로그래머스 [정렬]

### H-index ###
def solution(citations):
    lenC = len(citations)
    
    citations.sort()
    
    for i in range(lenC):
            if citations[i] >= lenC - i: 
                #citations[i]: 논문의 인용 횟수, lenC - i: 인용된 논문 수 
                return lenC - i
            
    return 0


### 가장 큰 수 ###
#쉽지않다. .. 
def solution(numbers):
    #맨앞자리 큰 거 부터 놓으면 될거같은데,,
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


### K번째 수 ###
def solution(array, commands):
    answer = []
    
    for com in commands:
        arr_com = array[com[0]-1:com[1]]
        answer.append(sorted(arr_com)[com[2]-1])
    return answer


### 더 맵게 ###
import heapq

def solution(scoville, K):
    answer = 0
    
    #섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    
    heapq.heapify(scoville) # 기존 리스트를 힙으로 바꾸기
    
    while scoville[0] < K: # 힙은 알아서 정렬이 되기 때문에 가장 앞 원소가 K보다 크면 반복문 멈춰
        min = heapq.heappop(scoville) 
        min2 = heapq.heappop(scoville)*2
        heapq.heappush(scoville, min+min2)
        answer += 1
    
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer