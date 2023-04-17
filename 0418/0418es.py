#1 블랙잭
card = [int(x) for x in input().split()]


n = card[0]
M = card[1]

card_list= [int(x) for x in input().split()]

sum = 0
result = -1

for i in range(n) :
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum = card_list[i] + card_list[j] + card_list[k]

            if sum >= result and sum<=M:
                result = int(sum)

print(result)

#2 부분합
n = input()

for i in range(int(n)):
    n_sum = 0
    for j in str(i):
        n_sum += int(j);
    if i + n_sum == int(n):
        print(i)
        break
else:
    print(0)


#3 수학 비대면강의
a, b, c, d, e, f = map(int, input().split())
#ax+by=c
#dx+ey=f

sol = []
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a*i+b*j==c and d*i+e*j==f:
            sol = [i, j]
            break

print(sol[0],sol[1])



#어쩔수없는 수학과의 풀이 . . .^^
#어차피 틀렸다고 나오니까 안보셔도 돼요...
arr = [int(x) for (x) in input().split()]
# arr[0]: a [1]: b [2]: c [3]: d [4]: e [5]: f
a = arr[0]
d = arr[3]

for i in range(0,3):
    arr[i] = arr[i] * d

for i in range(3,6):
    arr[i] = arr[i] * a
    
x=0
y=0

y = arr[1] - arr[4]
con = arr[2] - arr[5]

if y :
    realY = con//y

if arr[0]:
    x = (arr[2] - arr[1]*realY) // arr[0]
print(int(x), int(realY))