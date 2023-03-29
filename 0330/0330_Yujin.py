# 1.설탕
b = int(input())
a = -1
n = 1
while n % 5 !=0:
    a = a + 1
    n = b - (3*a)
if n < 0 :
    print(-1)
else:
    k = n / 5
    print(int(a + k))



# 2.동주니
a = int(input())
arr = []
for i in range(a):
    d=int(input())
    arr.append(d)
arr.reverse()
arr_len = len(arr)
num=0
for j in range(arr_len-1):
    if  arr[j]<=arr[j+1]:
        num+=arr[j+1]-arr[j]+1
        arr[j+1]=arr[j]-1
    else:
        continue
print(num)





# 3.펜파인애플애플펜
# 틀렸다고 나옴 ;
n = int(input())
ppap = input()
arr = list(ppap)
num=0
for i in range(n):
    if i+4<=n:
        if arr[i]=='p':
            if arr[i+1]=='P':
                if arr[i+2]=='A':
                    if arr[i+3]=='p':
                        num+=1
                        arr[i+3]=='Z'
print(num)