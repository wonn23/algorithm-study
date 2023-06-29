############ 체육복
def solution(n, lost, reserve):
    new_reserve = list(set(reserve) - set(lost))   # 여벌 체육복을 가져온 학생이 도난당할 수도 있으니까 도난당한 여벌 소유자는 최종 여벌 소유자에서 제외
    new_lost = list(set(lost) - set(reserve))      # 도난당한 학생 중, 여벌이 있는 학생을 고려하여 해당 학생은 lost에서 제외
    remove_lost = []   # new_lost.remove를 해버리면 반복문이 끊김 -> remove_lost를 선언하여 제거하고자 하는 lost요소를 append
    for l in new_lost:    
        if (l-1 in new_reserve):
            new_reserve.remove(l-1)
            remove_lost.append(l)
            
        elif (l+1 in new_reserve):
            new_reserve.remove(l+1)
            remove_lost.append(l)
        else:
            pass
    final_lost = list(set(new_lost) - set(remove_lost))    # new_lost - remove_lost = 남은 lost의 요소
    answer = n - len(final_lost)   # 체육수업을 들을 수 있는 학생 수 = 전체 학생 수 - 최종 lost에 있는 학생 수
    return answer



############## 단속 카메라
def solution(routes):
    answer = 0
    # 진출이 낮은 순으로 정렬
    routes.sort(key = lambda x: (x[1], x[0]))
    camera = -30001   # 최소 카메라 위치 지점
    
    for r0, r1 in routes:
        if camera < r0:
            answer += 1    # answer: 필요한 카메라 개수
            camera = r1
        else:   # camera > r0
            pass
    
    return answer
        
        
    
    
            