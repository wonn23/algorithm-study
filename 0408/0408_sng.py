################## 10828 스택
N = int(input())
commands = [input() for _ in range(N)]
stack = []

def is_empty(stack):
    if len(stack) == 0:
        return True
    
for i in commands:
    if i[:4] == 'push':
        num = int(i[5:])
        stack.append(num)
    if i == 'pop':
        if is_empty(stack):
            print(-1)
        else:
            print(stack.pop(-1))
    if i == 'size':
        print(len(stack))
    if i == 'empty':
        if is_empty(stack):
            print(1)
        else:
            print(0)
    if i == 'top':
        if is_empty(stack):
            print(-1)
        else:
            print(stack[-1])
    
    
    ############### 10845 큐
    N = int(input())
commands = [input() for _ in range(N)]
stack = []

def is_empty(stack):
    if len(stack) == 0:
        return True
    
for i in commands:
    if i[:4] == 'push':
        num = int(i[5:])
        stack.append(num)
    if i == 'pop':
        if is_empty(stack):
            print(-1)
        else:
            print(stack.pop(0))
    if i == 'size':
        print(len(stack))
    if i == 'empty':
        if is_empty(stack):
            print(1)
        else:
            print(0)
    if i == 'front':
        if is_empty(stack):
            print(-1)
        else:
            print(stack[0])
    if i == 'back':
        if is_empty(stack):
            print(-1)
        else:
            print(stack[-1])
    
    