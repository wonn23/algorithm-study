# 최소 직사각형
def solution(sizes):
    answer = 0
    w = 0
    h = 0
    for i, j in sizes:
        if i > j:
            w = max(w, i)
        else:
            w = max(w, j)
        if i < j:
            h = max(h, i)
        else:
            h = max(h, j)
    answer = w * h

    return answer


# 모의고사
def solution(answers):
    answer = []
    num1 = [1, 2, 3, 4, 5] * 2000
    num2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    num1_answer = 0
    num2_answer = 0
    num3_answer = 0
    for i in range(len(answers)):
        if num1[i] == answers[i]:
            num1_answer += 1
        if num2[i] == answers[i]:
            num2_answer += 1
        if num3[i] == answers[i]:
            num3_answer += 1
    max_num = max(num1_answer, num2_answer, num3_answer)
    if max_num == num1_answer:
        answer.append(1)
    if max_num == num2_answer:
        answer.append(2)
    if max_num == num3_answer:
        answer.append(3)

    return answer


# 소수 찾기
import math
import itertools


def is_prime_num(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    num = list(numbers)
    prime_set = set()
    for i in range(1, len(num) + 1):
        a = list(itertools.permutations(num, i))
        for j in a:
            # 튜플 안의 문자열을 합치기
            combined = "".join(j)
            # 합친 문자열을 숫자로 변환
            number = int(combined)
            if is_prime_num(number):
                prime_set.add(number)
    answer = len(prime_set)
    return answer


# 카펫
def solution(brown, yellow):
    area = brown + yellow
    for i in range(1, area):
        width = area // i
        length = i
        if width + length == (brown + 4) // 2 and width * length == area:
            answer = [width, length]
            break
    return answer


# 피로도
from itertools import permutations


def solution(k, dungeons):
    answer = 0
    dungeons_list = list(permutations(dungeons, len(dungeons)))
    for dungeon in dungeons_list:
        max_dungeons = 0
        current_fatigue = k
        for min_fatigue, consume_fatigue in dungeon:
            if current_fatigue >= min_fatigue:
                current_fatigue -= consume_fatigue
                max_dungeons += 1
        answer = max(answer, max_dungeons)
    return answer


# 전력망 둘로 나누기

# 모음사전
