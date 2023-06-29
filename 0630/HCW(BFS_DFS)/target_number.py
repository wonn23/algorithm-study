def solution(numbers, target):
    q = [0]
    j = 0
    while j < len(numbers):  # 최대 데이터 수는 2**20 약 10**6 이하이므로 O(n**2) 써도 됨
        cal_list = []  # 각 인덱스가 증가하면서 계산된 값을 넣어줄 빈 리스트
        for i in q:  # q에서 제거하고 추가하는 방식은 오류발생함
            cal_list.append(i + numbers[j])  # 그래서 통째로 바꿔주는 코드가 나음
            cal_list.append(i - numbers[j])
        j += 1  # 인덱스를 for문 완료 후 올려주자
        q = cal_list
    return q.count(target)


print(solution([1, 1, 1, 1, 1], 3))
