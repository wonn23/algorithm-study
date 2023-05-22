#0523 프로그래머스 [완전탐색]

### 최소직사각형 ###
def solution(sizes):
    nonMax=[]
    maxLen=0
    
    for i,j in sizes:
        if i>j: 
            maxLen = max(maxLen,i)
            nonMax.append(j)
        else:
            maxLen = max(maxLen,j)
            nonMax.append(i)
    return maxLen * max(nonMax)


### 모의고사 ###
def solution(answers):
    answer = []
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt1, cnt2, cnt3 = 0, 0, 0

    for i in range(len(answers)):
        sol = answers[i]
        if sol == supo1[i % len(supo1)]:
            cnt1 += 1
        if sol == supo2[i % len(supo2)]:
            cnt2 += 1
        if sol == supo3[i % len(supo3)]:
            cnt3 += 1

    max_cnt = max(cnt1, cnt2, cnt3)
    if max_cnt == cnt1:
        answer.append(1)
    if max_cnt == cnt2:
        answer.append(2)
    if max_cnt == cnt3:
        answer.append(3)

    return answer

### 카펫 ###
def solution(brown, yellow):
    answer = []
    allSqu = brown + yellow

    for i in range(1,int(brown/2)):
        if allSqu % i == 0: #가로
            j = allSqu // i #세로
            if (i-2)*(j-2) == yellow: # i-2 : 노란색 가로 길이, j-2 : 노란색 세로 길이
                answer = [i,j]
                #print(i, j)
    return answer

### 피로도 ###
#그리디로 풀고싶다 ..  ..

from itertools import permutations

def solution(k, dungeons):
    dungeons_count = len(dungeons)
    dungeons_list = [i for i in range(dungeons_count)]
    
    for i in range(len(dungeons), 0, -1): #최대 던전수부터 0될때까지 하나씩 감소
        for dungeon in permutations(dungeons_list, i):
            print(dungeon)
            now = k #현재 피로도 
            
            check = True 
            for dun in dungeon:
                if now < dungeons[dun][0]: #피로도 부족해서 탐험 못함
                    check = False
                    break
                else:
                    now -= dungeons[dun][1] #dun 던전 탐험해서 피로도 소모
                    print(dun, dungeons[dun], now)
            if check:
                return i
            print('--------')


#나머지 두 문제는 추후에 수정할게요,,