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
        
