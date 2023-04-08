#### 큐! ######
n = int(input())
qlist = []
stack = []

for j in range(n):
    qorder = input()
    qlist.append(qorder)

for i in qlist:
    if 'push' in i:
        value = i.split()[1]
        stack.append(value)
    elif 'pop' in i:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(0))
    elif 'size' in i:
        print(len(stack))
    elif 'empty' in i:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in i:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    elif 'back' in i:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])






#########스택!########
n = int(input())
qlist = []
stack = []

for j in range(n):
    qorder = input()
    qlist.append(qorder)

for i in qlist:
    if 'push' in i:
        value = i.split()[1]
        stack.append(value)
    elif 'pop' in i:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(-1))
    elif 'size' in i:
        print(len(stack))
    elif 'empty' in i:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif 'top' in i:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])