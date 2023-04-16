### 2798 블랙잭 ###

a,b = map(int, input().split())
my_list = list(map(int,input().split()))
three_card = []
max_num = 0
for i in range(len(my_list)):
    for j in range(i+1,len(my_list)):
        for k in range(j+1,len(my_list)):
            three_card.append((my_list[i],my_list[j],my_list[k]))
for p in three_card:
    if sum(p)<=b and max_num < sum(p):
            max_num = sum(p)
print(max_num)

### 2231 분해합 ###

n = input()

for i in range(int(n)):
    sum_inx = 0
    for j in str(i):
        sum_inx += int(j)
    if int(n) == sum_inx + i:
        print(i)
        break
else:
    print(0)

### 19532 수학은 비대면강의입니다. ###
a,b,c,d,e,f = map(int,input().split())

x = (c*e-b*f)/(a*e-b*d)
y = (a*f-c*d)/(a*e-b*d)
print(int(x),int(y))