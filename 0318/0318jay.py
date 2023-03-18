#실습 - 연속된 부분합의 최댓값
import sys
INITIAL_VALUE = sys.maxsize * -1

def bruteForce(arr):
    result = INITIAL_VALUE
    arr_length = len(arr)  # 5가 arr_length에 할당
    max_num = arr[0] # 첫시작의 숫자 임의로 지정 
    
    # i와 j는 연속된 부분의 길이를 결정해요.
    for i in range(arr_length): #배열 길이만큼 반복문 실행
        
        current_sum = 0 #현재의 값 0부터 시작
        
        for j in range(i, arr_length): #i부터 반복문 실행
            
            current_sum += arr[j] #반복문 실행 시 current_sum에 값 저장
            
            result = max(result, current_sum)
    
    return result


def main():
    arr = [int(x) for x in input().split()]
    print(bruteForce(arr))

if __name__ == "__main__":
    main()



    #############미션1 - 문장 속 단어 찾기
def countWord(sentence, word):
    result = sentence.count(word)
    return result


def main():
    sentence = input()
    searchingWord = input()

    print(countWord(sentence, searchingWord))


if __name__ == "__main__":
    main()

################미션2 - 가장 가까운 별 찾기
import math
import sys

# 두 별 사이의 거리를 구해주는 함수예요.
def getDistance(p1, p2):
    return math.sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )


# 가장 가까운 두 별 사이의 거리를 계산하는 함수예요.
def findStar(points):
    result = sys.maxsize
    n = len(points) # 5를 n에 할당
    
    for i in range(n):

        dist = 0 

        for j in range(i):

            dist = getDistance(points[i],points[j]) #dist 값 업데이트
            
            result = min(result,dist)

    return result

def main():
    
    # 별들의 위치를 저장하는 리스트예요.
    points = [] #[(1,1),(2,8),(9,4),(4,8),(0,1)]로 저장
    
    for i in range(5) :
        line = [int(x) for x in input().split()]
        points.append( (line[0], line[1]) )

    print("%.3lf" % findStar(points))

if __name__ == "__main__":
    main()

####################미션3 - 균형 맞추기
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
        
        a = sum(combination)
        b = wholeSum - a

        minimumAB = min(minimumAB, abs(a-b))
    
    return minimumAB


def main():
    arr = [int(x) for x in input().split()]
    print(minimumDifference(arr))

if __name__ == "__main__":
    main()