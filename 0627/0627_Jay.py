#큰수 만들기 (그리다알고리즘)
def solution(number, k):
    stack = []
    
    for i in number:
        while stack and stack[-1] < i and k > 0:
            stack.pop()
            k -= 1
        
        stack.append(i)
    
    # 주어진 숫자가 이미 가장 큰 수로 주어져서 k가 0보다 클때, 그냥 k값만큼 빼주자.
    if k > 0:
        ans = stack[:-k]
    
    return ''.join(ans)
