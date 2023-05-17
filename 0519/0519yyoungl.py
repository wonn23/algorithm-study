### 0519 스터디


### Heap - 더 맵게

## deque로 푼 것

from collections import deque

def solution(scoville, K):
    answer = 0
    scoville = deque(sorted(scoville))
    while any(sco < K for sco in scoville):
        if len(scoville) < 2:
            return -1
        
        one = scoville.popleft()
        two = scoville.popleft()
        scoville.append(one + two * 2)
        
        scoville = deque(sorted(scoville))
        answer += 1
        
    return answer 

## 사실 heap으로 풀었어야 했다..

import heapq

def solution(scoville, K):
    answer = 0
    scoville = sorted(scoville)
    while any(sco < K for sco in scoville):
        if len(scoville) < 2:
            return -1
        
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        answer += 1
        
    return answer

### K번째 수

def solution(array, commands):
    answer = []
    for x in commands:
        answer.append(sorted(array[x[0]-1:x[1]])[x[2]-1])
    return answer


### 가장 큰 수

def solution(numbers):
    numbers = list(map(str, numbers))
    
    # 숫자를 정렬하는 기준을 변경하여 정렬
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    # 리스트의 숫자들을 이어붙여서 문자열로 반환
    answer = ''.join(numbers)
    
    # answer가 0으로 시작하는 경우를 처리하기 위해 int로 변환 후 다시 문자열로 변환
    return str(int(answer))



### 정렬 - H-Index

def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    n = len(citations)
    for i in range(n):
        if citations[i] < i+1 :
            break
        answer+=1
    return answer
