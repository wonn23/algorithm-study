def solution(distance, rocks, n):   
    left = 0
    right = distance
    
    rocks.sort()
    rocks.append(distance) 
    
    while left <= right:
        mid = (left + right) // 2
        
        delete = 0 # 제거한 바위의 개수
        prev_rock = 0 # 이전 돌의 위치

        for rock in rocks:
            dist = rock - prev_rock # 현재 돌과 이전 돌 사이의 거리를 저장
            
            if dist < mid:
                delete += 1
                if delete > n:
                    break
            
            else:
                prev_rock = rock
        
        if delete > n:
            right = mid -1
        else:
            answer = mid
            left = mid + 1
    return answer


print(solution(25,[2,14,11,21,17],2))