####14495.피보나치 어쩌구저쩌구#####
##### 아침부터 안과 갔다오고 좀 쉬느라.. 문제를 다 풀어보긴 했지만 제대로 푼 건 시간상 이거뿐..,####
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