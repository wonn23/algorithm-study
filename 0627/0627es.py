#0627 은석 그리디

#체육복
def solution(n, lost, reserve):
    reserve_list = set(reserve) - set(lost)
    # reserve 리스트에서 lost 리스트에 있는 학생들을 제외
		# 여분 가진 애들 중에 잃어버린 학생 제외

    lost_list = set(lost) - set(reserve)
		# lost 리스트에서 reserve 리스트에 있는 학생들을 제외
		# 체육복 잃어버렸는데 여분 못받은 애들
    
    for student in reserve_list:
        if (student - 1) in lost_list:
            lost_list.remove(student - 1)
        elif (student + 1) in lost_list:
            lost_list.remove(student + 1)
    return n - len(lost_list)


#섬 연결하기
def solution(n, costs):
    answer = 0
    visited = [0] * n
    costs.sort(key = lambda x: x[2]) # 비용 기준으로 오름차순 정렬
    visited[costs[0][0]] = 1 # cost 가장 작은 애가 출발점
    
    while(1):
        if sum(visited) == n:
            break
        for cost in costs:
            if visited[cost[0]] and visited[cost[1]]:
                continue
            elif visited[cost[0]] or visited[cost[1]]:
                answer += cost[2]
                visited[cost[0]] = 1
                visited[cost[1]] = 1
                break
                
    return answer