# 입국심사

def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    while left <= right:
        mid = (left+ right) // 2
        people = 0
        for time in times:
            people = people + (mid // time)

        if people >= n:
            answer = mid
            right = mid - 1
        elif people < n:
            left = mid + 1
            
    return answer

print(solution(6, [7,10]))