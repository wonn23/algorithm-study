##################################1번문제
def getSlope(point1, point2):
    if point1[0] == point2[0]:
        return 0
    return abs( (point1[1] - point2[1]) / (point1[0] - point2[0]) )


def findMaxSlope(points):
    # x값을 기준으로 점들을 정렬해 주세요.
    sortedPoints = points.sort(key = lambda x : x[0])
    
    maxSlope = float('-inf') #-무한대
    # x값을 기준으로 인접한 두 점의 기울기를 모두 구해서 최대 기울기를 찾아주세요.
    for slope in range(len(points)-1):
        maxSlope = max(maxSlope,getSlope(points[slope], points[slope+1]))
    
    # maxSlope 값을 소수점 4번째 자리에서 반올림해서 반환해 주세요.
    return maxSlope


def main():
    n = int(input())
    
    points = []
    for i in range(n):
        point = [int(x) for x in input().split()]
        points.append(point)
        
    print("%.3lf" % findMaxSlope(points))

if __name__ == "__main__":
    main()

######################### 2번문제
def maximumPeopleUsage(times):
    result = 0
    
    times.sort(key=lambda x: (x[1], x[0]))
    
    # 컴퓨터를 사용할 수 있는 최대 인원수를 계산해 주세요.
    student = [0] 
    for i in range(len(times)):
        if times [i][0] >= student[-1]:
            student.append(times[i][1])
    
    return len(student) - 1

def main():
    n = int(input())
    times = []
    for _ in range(n):
        time = [int(x) for x in input().split()]
        times.append(time)
    print(maximumPeopleUsage(times))

if __name__ == "__main__":
    main()

############################### 3번문제
# 모르겠어요 이해가 안가요...

################## 4번문제
def coins(n):
    coins = [10, 50, 100, 500] 
    coins.sort(reverse=True) 
    
    result = {x: 0 for x in coins}

    for coin in coins:
        coinCount = n // coin
        
        n -= coin * coinCount
        
        result[coin] = coinCount
        
    return result


def main():
    n = int(input())
    cnt = 0
    for value in coins(n).values():
        cnt+=value
    print(cnt)


if __name__ == "__main__":
    main()

