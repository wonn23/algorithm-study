### 2839번 설탕 배달 ###

n = int(input()) # 설탕

result = 0 # 봉지 수

while n >= 0:
    if n % 5 == 0: # 5로 나눈 나머지가 0인 경우
        result += n // 5 # 5로 나눈 몫을 추가
        print(result)
        break
    n -= 3 # 설탕이 5의 배수가 될때까지 반복
    result += 1 # 봉지 추가
else:
    print(-1) # while문이 거짓이 되면 -1 출력

### 2847번 게임하는 동준이 ###
n = int(input())
my_list = []
for i in range(n): 
    game_level = int(input())
    my_list.append(game_level)
i = 0
result = 0
my_list = my_list[::-1] # 가장 큰 수부터 정렬하기 위해 배열을 거꾸로함
for _ in range(n-1):
    while my_list[i] <= my_list[i+1]:
        my_list[i+1] -= 1
        result += 1
    i += 1
    
print(result)

### 15881번 Pen Pineapple Apple Pen ###

num = int(input())
string = input()
max_num = string.split('pPAp')
print(len(max_num)-1)
