# 3월 18일 스터디 코드 리뷰 허창원

### 미션 1 - 문장 속 단어 찾기

def countWord(sentence, word): # 한글은 띄어쓰기 단위로 되어있으므로 in을 사용해서 단어를 찾음.
    count = 0
    a=sentence.split(' ')
    for i in a:
        if word in i:
            count +=1
    return count

def main():
    sentence = input()
    searchingWord = input()
    
    print(countWord(sentence, searchingWord))


if __name__ == "__main__":
    main()







### 미션 2 - 가장 가까운 별 찾기

import math
import sys

# 두 별 사이의 거리를 구해주는 함수예요.
def getDistance(p1, p2):
    return math.sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )


# 가장 가까운 두 별 사이의 거리를 계산하는 함수예요.
def findStar(points):
    result = sys.maxsize # min, max비교할 때 max=0 이나 min = 999999999999로 설정해두면 문제가 생긴다.
    n = len(points)

    for i in range(n):
        for j in range(i+1,n): # i=0에서 시작하면 같은 점을 비교하므로 안된다.
            if result > getDistance(points[i], points[j]):
                result=getDistance(points[i], points[j])
    return result


'''
가장 좋지 않은 방법은 큰 값을 설정할 때 9999999와 같은 임의의 값을 지정하는 것이다. 이렇게 하면 문제가 발생 할 수 있다.
파이썬의 숫자형은 임의 정밀도(Arbitrary-Precision)을 지원하며 사실상 무한대의 값을 지정할 수 있다. 아무리 큰 수라 할지라도 얼마든지 더 큰 수가 지정될 수 있으므로 변수에 임의의 큰 값으로 초기화 하는 것은 지양해야 한다.
'''
def main():
    
    # 별들의 위치를 저장하는 리스트예요.
    points = []
    
    for i in range(5) :
        line = [int(x) for x in input().split()]
        points.append( (line[0], line[1]) )
    
    print("%.3lf" % findStar(points))

if __name__ == "__main__":
    main()







### 미션 3 - 균형 맞추기

def powerSet(s): # 14번 줄에 s는 리스트 형태로 들어올 것이란 것을 알 수 있다.
    powerset = []
    x = len(s) # s의 원소의 개수
    for i in range(1 << x): # 비트연산자 '1 << x'는 1을 x만큼 비트를 왼쪽으로 이동시킨다는 뜻이다. 결과적으로 2**x이고 부분집합의 개수를 뜻한다.
        powerset.append([s[j] for j in range(x) if (i & (1 << j))]) # 리스트 함축을 통해 powerset은 리스트를 원소로 가진 리스트인 것이다.
# powerset 함수에 append는 8번 시행되는 것이고 리스트 함축의 원소는 [1,2,3] 중에서 선택되는 것이다.
    return powerset


def minimumDifference(arr):
    if len(arr) == 0:
        return 0
    
    # 주어진 리스트를 분할하는 가능한 모든 조합을 구해요.
    combinations = powerSet(arr) # [[],[1],[2],[3],[1,2],[2,3],[1,3],[1,2,3]]
    
    # 주어진 리스트의 모든 원소들의 합을 구해요.
    wholeSum = sum(arr) # sum([1,2,3]) = 6
    
    # A그룹과 B그룹의 차이 최솟값을 초기화해요.
    # 최솟값은 아무리 커도 리스트 내 최댓값을 넘지 않으니, 리스트 내 최댓값으로 초기화해요.
    minimumAB = max(arr) # max([1,2,3]) = 3
    
    # 반복문을 통해 모든 조합을 탐색하여 그룹의 차이를 구해주세요.
    for i in range(len(combinations)):
        min_sum = abs(sum(combinations[i]) - sum(combinations[len(combinations)-1-i]))
        if minimumAB > min_sum:
            minimumAB = min_sum
    
    return minimumAB


def main():
    arr = [int(x) for x in input().split()]
    print(minimumDifference(arr))

if __name__ == "__main__":
    main()
