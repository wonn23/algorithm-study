### 2798 블랙잭 ###

n,m = map(int, input().split())
my_list = list(map(int,input().split()))
three_card_sum = 0
max_num_list = []
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            three_card_sum = my_list[i]+my_list[j]+my_list[k]
            if three_card_sum <= m:
                max_num_list.append(three_card_sum)
print(max(max_num_list))

### 2231 분해합 ###

n = input()

for i in range(int(n)):
    sum_idx = 0 # 각 자리 수의 합 매번 초기화 해줌
    for j in str(i):
        sum_idx += int(j) # 각 자리 수의 합
    if int(n) == sum_idx + i: # 216 == (1+9+8) +198
        print(i) # 가장 작은 생성자이므로 답이나오면 바로 break
        break
else:
    print(0)

### 19532 수학은 비대면강의입니다. ###
a,b,c,d,e,f = map(int,input().split()) # 이거는 인터넷 검색해서 풀었음

x = (c*e-b*f)/(a*e-b*d)
y = (a*f-c*d)/(a*e-b*d)
print(int(x),int(y))