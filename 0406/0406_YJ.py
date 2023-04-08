####14495.피보나치 어쩌구저쩌구#####
inputvalue = int(input())
if inputvalue ==1 or inputvalue==2 or inputvalue==3:
    print(1)
else:
    x1=1
    x2=1
    x3=1
    x4 = x1+x3
    for i in range(4, inputvalue):
        x1=x2
        x2=x3
        x3=x4
        x4=x1+x3
        print(x1,x2,x3,x4)



#####1026.국왕김지민######
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sumvalue=0
for i in range(n):
    maxb=max(b)
    mina=min(a)
    sumvalue+=mina*maxb
    b.remove(max(b))
    a.remove(min(a))
print(sumvalue)




######1904.타일#######
n= int(input())
Table = [0 for i in range(n+1)]

if n==1:
    print(1)
elif n==2:
    print(2)
else:
    Table[1] = 1
    Table[2] = 2
    for i in range(3, n+1):
        Table[i] = (Table[i-2] + Table[i-1])%15746
    print(Table[n])