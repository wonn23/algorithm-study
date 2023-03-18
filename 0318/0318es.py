# 이은석_0318 스터디 [완전 탐색]

#######################미션1
# 문장에서 단어의 개수를 세는 함수를 작성해 보세요.
def countWord(sentence, word):
    count = 0
    sentence = sentence.split(' ') #문장 배열 만들기
    for i in range(len(sentence)) : 
        if word in sentence[i]: #찾으려는 단어가 인덱스에 포함될 경우 count +1
            count+=1
    return count


def main():
    sentence = input()
    searchingWord = input()
    
    print(countWord(sentence, searchingWord))


if __name__ == "__main__":
    main()


########################미션2
import math
import sys

# 두 별 사이의 거리를 구해주는 함수예요. (두 점 사이의 거리 공식 이용)
def getDistance(p1, p2):
    #print(p1,p2)
    return math.sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )


# 가장 가까운 두 별 사이의 거리를 계산하는 함수예요.
def findStar(points):
    result = sys.maxsize
    n = len(points)
    
    # 가장 가까운 두 별을 찾고, 거리를 계산해 주세요.
    for i in range(0,n):
        for j in range(i+1,n):
            a = getDistance(points[i],points[j]) 
            #print(a)
            if a <= result :
                result = a
    
    return result


def main():
    
    # 별들의 위치를 저장하는 리스트예요.
    points = []
    
    for i in range(5) :
        line = [int(x) for x in input().split()]
        points.append( (line[0], line[1]) )
    
    print("%.3lf" % findStar(points))

if __name__ == "__main__":
    main()



###################미션3
def powerSet(s):
    powerset = []
    x = len(s)
    for i in range(1 << x):
        powerset.append([s[j] for j in range(x) if (i & (1 << j))])
    return powerset


def minimumDifference(arr):
    if len(arr) == 0:
        return 0
    
    # 주어진 리스트를 분할하는 가능한 모든 조합을 구해요.
    combinations = powerSet(arr)
    
    # 주어진 리스트의 모든 원소들의 합을 구해요.
    wholeSum = sum(arr)
    
    # A그룹과 B그룹의 차이 최솟값을 초기화해요.
    # 최솟값은 아무리 커도 리스트 내 최댓값을 넘지 않으니, 리스트 내 최댓값으로 초기화해요.
    minimumAB = max(arr)
    
    # 반복문을 통해 모든 조합을 탐색하여 그룹의 차이를 구해주세요.
    for combination in combinations:
        combSum = sum(combination) # combination 그룹의 원소 합
        restSum = wholeSum - combSum # combination말고 다른 그룹의 원소 합
        
        diff = abs(combSum - restSum) # 두 그룹의 차의 절댓값 구하는 abs 함수 사용
       # print (combination,combSum,restSum,diff)

        if diff < minimumAB :
            minimumAB = diff
        
    return minimumAB


def main():
    arr = [int(x) for x in input().split()]
    print(minimumDifference(arr))

if __name__ == "__main__":
    main()