########## 더 맵게
import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    
    
    answer = 0
    while scoville[0] < K:
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer




############k번째 수
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
        
    return answer




#####################가장 큰 수
# sorted 함수에 대해 공부하기
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
    
    
    