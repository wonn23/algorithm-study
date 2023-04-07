#0408 백준 큐, 스택

#1. 큐 https://www.acmicpc.net/problem/10845

n= int(input())
str1 = [] #명령 입력

for _ in range(n):
    str1.append(input())

Q = []

for i in str1:
    i = i.split()
    if i[0] == 'push':
        Q.append(int(i[1]))

    elif i[0] == 'front':
        if Q :
            print(Q[0])
        else :
            print(-1)
    
    elif i[0] == 'back':
        if Q :
            print(Q[-1])
        else :
            print(-1)

    elif i[0] == 'size':
        print(len(Q))

    elif i[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    
    elif i[0] == 'pop':
        if Q:
            print(Q.pop(0))
        else:
            print(-1)


#2 스택 https://www.acmicpc.net/problem/10828
n= int(input())
str1 = [] #명령 입력

for _ in range(n):
    str1.append(input())

stack = []

for i in str1:
    i = i.split()
    if i[0] == 'push':
        stack.append(int(i[1]))

    elif i[0] == 'size':
        print(len(stack))

    elif i[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    
    elif i[0] == 'pop':
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)

    elif i[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)