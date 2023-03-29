#### 0330 스터디
####  설탕 배달
n = int(input())
count = 0

while n>0:
    if n%5 == 0:
        count += n//5
        break
    elif n==1 or n==2:
        count = -1
        break
    else:
        n -= 3
        count += 1

print(count)


#### 게임을 만든 동준이
n = int(input())
level = []
cnt = 0
for i in range(n):
    level.append(int(input()))

for i in range(1, n):
    if level[-i] <= level[-i-1]:
        cnt += level[-i-1] - level[-i] + 1
        level[-i-1] = level[-i] - 1

print(cnt)


#### 펜파인애플애플펜
string = input()
strcheck = []

for i in range(len(string)):
    strcheck.append(string[i])
    if strcheck[-1] == 'P' and strcheck[-4: ] == list('PPAP'):
        del strcheck[-4: ]
        strcheck.append('P')
if strcheck == list('PPAP') or strcheck == list('P'):
    print('PPAP')
else:
    print("NP")