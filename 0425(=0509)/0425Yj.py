#####17204.죽음의게임#######
count,num=map(int,input().split())
numlist=[]
for i in range(count):
    a = int(input())
    numlist.append(a)
newnum=0
t=0
for i in range(count):
    if newnum != num:
        newnum=numlist[newnum]
        t+=1
    else:
        print(t)
        break
else:
    print(-1)


#####1436.영화감독 숌######
n = int(input())
t = 1
k = 665
while t<=n:
    k=int(k)+1
    if '666' in str(k):
        t=t+1
print(k)