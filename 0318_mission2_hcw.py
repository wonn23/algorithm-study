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
