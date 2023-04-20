###백준 10845 큐###

import sys
from collections import deque

queue = deque([])

def process_queue(command):
    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == "back":
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
            
n = int(input())
for i in range(n):
    command = sys.stdin.readline().split()
    process_queue(command)


###백준 10828 스택 ###

import sys

stack = []
'''
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
def process_stack(command): 
    if command[0] == "push":
        stack.append(int(command[1]))

    elif command[0] == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print("-1")

    elif command[0] == "size":
        print(len(stack))

    elif command[0] == "empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")

    elif command[0] == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print("-1")
            
n = int(sys.stdin.readline())

for i in range(n):
    command = sys.stdin.readline().split()
    process_stack(command)