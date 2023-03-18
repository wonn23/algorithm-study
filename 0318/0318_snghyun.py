# 이승현_0318 스터디 [완전 탐색]

######################## 미션 1
# 문장에서 단어의 개수를 세는 함수를 작성해 보세요.
def countWord(sentence, word):
    return sentence.count(word)


def main():
    sentence = input()
    searchingWord = input()
    
    print(countWord(sentence, searchingWord))


if __name__ == "__main__":
    main()
    



    
######################## 미션 2
import math
import sys

# 두 별 사이의 거리를 구해주는 함수예요.
def getDistance(p1, p2):
    return math.sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )


# 가장 가까운 두 별 사이의 거리를 계산하는 함수예요.
def findStar(points):
    result = sys.maxsize
    n = len(points)
    
    # 가장 가까운 두 별을 찾고, 거리를 계산해 주세요.
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            
            if (result > getDistance(points[i],points[j])):
                result = getDistance(points[i],points[j])
            else:
                pass
    
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
    
    
    
    
############################# 미션 3
def powerSet(s):
    powerset = []
    x = len(s)
    for i in range(1 << x):    
        powerset.append([s[j] for j in range(x) if (i & (1 << j))])
    return powerset


def minimumDifference(arr):
    if len(arr) == 0:
        return 0

    combinations = powerSet(arr)
    
    # wholeSum = sum(arr)

    minimumAB = max(arr)
    
    # 반복문을 통해 모든 조합을 탐색하여 그룹의 차이를 구해주세요.
    for i in range(len(combinations)):
        complement = list(set(arr) - set(combinations[i]))  # 차집합 (A그룹을 combinations[i]라고 할 때, B그룹은 combinations[i]에 속한 원소를 제외한 나머지 원소의 집합)
        difference = abs(sum(complement) - sum(combinations[i]))  # A그룹의 원소 합과 B그룹의 원소 합 의 차이
        if (minimumAB > difference): 
            minimumAB = difference
        else:
            pass
    
    return minimumAB


def main():
    arr = [int(x) for x in input().split()]
    print(minimumDifference(arr))


if __name__ == "__main__":
    main()

