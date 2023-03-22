## 3월 23일 스터디 - 알고리즘 스타 I 탐욕적 기법

#### 미션1 - 가장 큰 기울기  찾기

def getSlope(point1, point2):
    if point1[0] == point2[0]:
        return 0
    return abs( (point1[1] - point2[1]) / (point1[0] - point2[0]) )


def findMaxSlope(points):
    # x값을 기준으로 점들을 정렬해 주세요.
    #print(points)
    sortedPoints = sorted(points, key = lambda x: x[0])
    #print(sortedPoints)
    
    maxSlope = float('-inf') #max를 음의 무한대 값으로 설정함
    # x값을 기준으로 인접한 두 점의 기울기를 모두 구해서 최대 기울기를 찾아주세요.
    # 왜 이렇게 하는가? 기울기는 (y 값의 차이 / x값의 차이) 로 구하기 때문!!
    # 가장 큰 기울기를 가지려면 분모 (x 값의 차이)가 최소여야 하기 때문에 x로 정렬하고, 인접한 점끼리 기울기를 구한다
    
    for i in range(len(sortedPoints)-1):
        slope = getSlope(sortedPoints[i], sortedPoints[i+1])
        if slope > maxSlope:
            maxSlope = slope

    # maxSlope 값을 소수점 4번째 자리에서 반올림해서 반환해 주세요.
    return round(maxSlope, 3) # 소수 셋째 자리까지 표현


def main():
    n = int(input())
    
    points = []
    for i in range(n):
        point = [int(x) for x in input().split()]
        points.append(point)
        
    print("%.3lf" % findMaxSlope(points))

if __name__ == "__main__":
    main()



#### 미션2 - 컴퓨터 배정


def maximumPeopleUsage(times):
    result = 0
    
    # 이용 시간을 정렬해요.
    # 종료 시간이 빠른 순서 & 시작 시간이 빠른 순서
    times.sort(key=lambda x: (x[1], x[0]))
    
    # 컴퓨터를 사용할 수 있는 최대 인원수를 계산해 주세요.
    last = 0
    for i in range(len(times)):
        if times[i][0] >= last:
            result += 1
            last = times[i][1]
    
    return result


def main():
    n = int(input())
    times = []
    for _ in range(n):
        time = [int(x) for x in input().split()]
        times.append(time)
    print(maximumPeopleUsage(times))

if __name__ == "__main__":
    main()



#### 미션3 - 컴퓨터 배정 심화

def minimunComputerNeeds(times):
    result = 0
    # 이용 시간을 정렬해요.
    # 종료 시간이 빠른 순서 & 시작 시간이 빠른 순서
    sortedTimes = sorted(times, key = lambda x: (x[1],x[0]))
    # print(sortedTimes)
    
    # 구매해야 하는 컴퓨터의 최소 개수를 계산해 주세요.
    last = [0]
    for x in range(len(sortedTimes)):
            # last 배열에서 조건을 만족하는 첫 번째 값의 index 찾기
        if any(y <= sortedTimes[x][0] for y in last) == True:
            idx = next(i for i, val in enumerate(last) if val <= sortedTimes[x][0]) 
            last[idx] = sortedTimes[x][1]
        else:
            last.append(sortedTimes[x][1])
        
        # print(last)


    return len(last) -1


def main():
    n = int(input())
    times = []
    for _ in range(n):
        time = [int(x) for x in input().split()]
        times.append(time)
    print(minimunComputerNeeds(times))

if __name__ == "__main__":
    main()




#### 미션4 - 동전 거스름돈

def coins(n):
    coins = [10, 50, 100, 500]
    coins.sort(reverse = True)
    coinCount = 0 
    result = {x: 0 for x in coins}

    for coin in coins:
        result[coin] = n // coin
        n = n % coin

    return result

def main():
    n = int(input())
    cnt = 0
    for value in coins(n).values():
        cnt+=value
    print(cnt)

if __name__ == "__main__":
    main()
