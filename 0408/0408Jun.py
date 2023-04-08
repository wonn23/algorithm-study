#백준0408 - 황준성



#---10845 – 큐---



import sys
from collections import deque

queue = deque()

n = int(sys.stdin.readline())

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.append(int(command[1]))

    elif command[0] == 'pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())

    elif command[0] == 'size':
        print(len(queue))

    elif command[0] == 'empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])

    elif command[0] == 'back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])



#---10828 – 스택---



stack = []

import sys
n = int(sys.stdin.readline())  
#입출력 속도 비교 : sys.stdin.readline > raw_input() > input()

stack=[]
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.append(int(command[1]))

    elif command[0] == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)

    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])


