# K번째 수
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1] - 1
        idx = commands[i][2] - 1
        Slice = sorted(array[start : end + 1])
        answer.append(Slice[idx])
    return answer


# 가장 큰 수
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    # [9, 5, 34, 3, 30 ] 1000미만
    # 999 555 343434 333 303030

    return str(int("".join(numbers)))  # 이 문제는 너무 어렵다


# H-index


def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    for i in range(n):
        h_index = n - i  # 5 4 3 2 1
        if citations[i] >= h_index:
            answer = h_index
            break
    return answer


# 더 맵게

import heapq


def solution(scoville, K):
    answer = 0
    result = []
    for value in scoville:
        heapq.heappush(result, value)

    while result[0] < K:
        if len(result) < 2:
            return -1
        answer += 1
        add_scovile = heapq.heappop(result) + heapq.heappop(result) * 2
        heapq.heappush(result, add_scovile)
    return answer
