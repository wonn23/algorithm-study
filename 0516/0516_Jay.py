#같은 숫자는 싫어
def solution(arr):
    ans = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            ans.append(arr[i])
    return ans

#올바른 괄호
#괄호를 올바르게 열고 닫는것을 확인하는 문제. 괄호로만 이루어진 입력값이 주어졌을때, 
# 올바른 괄호이면 true 아니면 false를 return 해야함. 
# 괄호 방향을 1, -1 로 생각하면 짝지어진 괄호의 총합은 항상 0이 되니까 괄호를 숫자로 지정해서 계산하면 되겠다. 
# 맞나? 음...  3번째 예시도 0인데? 아 -1로 시작하면 무조건 false로 return 하자
def solution(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0

#기능개발
# 100을 기준으로 봤을때, 100 - progress 는 남은 작업이고 여기에 스피드를 나누면 배포일수가 나온다.
# 배포일수를 기준으로 배열를 만들고 앞에 배열이 뒤의 배열들 보다 크거나 같으면 카운트를 하고 뒤의 값이 커지는 순간 카운트를 리턴하고 다시 앞의 과정을 진행하면 될 것 같다.
#아니 근데 이미 백분율 비율이 다 통일인데 그냥 프로그래스랑 스피드 100 될때까지 더해서 첫번째 값이 100이 될때 100 보다 큰 숫자들 카운트 하면 될것같은데... 
import math

def solution(progresses, speeds):
    stack = []
    
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        count = 0
        
        while progresses and 100 <= progresses[0]:
            count += 1
            del progresses[0]
            del speeds[0]
        
        if count != 0:
            stack.append(count)
            
    return stack