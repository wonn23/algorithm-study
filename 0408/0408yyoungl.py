##지난주에 맡은 문제만 풀었어서 이번에 나머지 문제들도 다 풀어서 올립니다요 ~!

##백준 1904 01타일


n = int(input())

table = [0 for _ in range(n+2)]
table[1] = 1
table[2] = 2

for x in range(3, n+1):
    table[x] = (table[x-1] + table[x-2])%15746
    
print(table[n])


##백준 14495 피보나치 비스무리한 수열

n = int(input())
table = [1] * 117
# 이거 table[1], table[2], table[3] = 1 이렇게 선언해도 되나?
if n > 3:
    for x in range(4, n+1):
        table[x] = table[x-1] + table[x-3]

print(table[n])


##백준 10845 큐(Queue)
##for문 돌려서 하면 오류 뜸!! 그래서 stdin import 해서 썼습니다

from sys import stdin

queue = []
n = int(stdin.readline())

for _ in range(n):
    com = stdin.readline().split()
    if com[0] == 'push': queue.append(int(com[1]))
    elif com[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif com[0] == 'size': print(len(queue))
    elif com[0] == 'empty':
        if len(queue) == 0 : print(1)
        else: print(0)
            
    elif com[0] == 'front':
        if len(queue) == 0 : print(-1)
        else: print(queue[0])
    elif com[0] == 'back':
        if len(queue) == 0 : print(-1)
        else: print(queue[-1])


##백준 10828 스택(Stack)
from sys import stdin

stack = []
n = int(stdin.readline())

for _ in range(n):
    com = stdin.readline().split()
    if com[0] == 'push': stack.append(int(com[1]))
    elif com[0] == 'pop':
        if stack:
            print(stack.pop())
        else: print(-1)
    elif com[0] == 'size': print(len(stack))
    elif com[0] == 'empty':
        if len(stack) == 0 : print(1)
        else: print(0)
    elif com[0] == 'top':
        if len(stack) == 0 : print(-1)
        else: print(stack[-1])
        
