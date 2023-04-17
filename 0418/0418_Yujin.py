# 집힛디 도움 아예 안 받고 문제 푼 게 얼마만인지 ,, 눈물나네 진짜ㅜㅜ 
# 알고리즘의 즐거움을 오랜만에 느끼고 갑니다^^ 총총~
# 가끔 숨통 트이게 이렇게 쉬운 문제도 풀어가며 합세다..

########2798.블랙잭#########
a,n = map(int,input().split())
c = list(map(int,input().split()))
#n의 숫자를 넘지 않게 c리스트에서 3개 뽑기
t=0
for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            if c[i]+c[j]+c[k]>t and c[i]+c[j]+c[k]<=n:
                t=c[i]+c[j]+c[k]
               
print(t)






#########2231.분해합##########
n=int(input())
q=[]
for i in range(n):
    a = [int(t) for t in str(i)]
    b = ''.join(str(i) for i in a)
    k=int(b)
    for j in a:
        k=k+j
    if k==n: #처음에 이 if 문은 for문 안에 넣어서 틀렸었음 그럼 다 더하기 전에 if문이 실행되기 때문
        q.append(b)
        break
if len(q)==0:
    print(0)
else:
    print(min(q))





##########19532.수학은 어쩌고저쩌고##########
numlist=list(map(int,input().split()))
a=numlist[0]
b=numlist[1]
c=numlist[2]
d=numlist[3]
e=numlist[4]
f=numlist[5]
for x in range(-999,1000):
    for y in range(-999,1000): #처음에 999까지로 했다가 틀렸었음
        if a*x+b*y == c:
            if d*x+e*y == f:
                print(x,y)
