#탐욕적 기법 - 황준성

#---미션1 - 가장 큰 기울기 찾기---



def getSlope(point1, point2):
    if point1[0] == point2[0]:
        return 0
    return abs( (point1[1] - point2[1]) / (point1[0] - point2[0]) )


def findMaxSlope(points):
    # x값을 기준으로 점들을 정렬해 주세요.
    sortedPoints = sorted(points)
    
    maxSlope = float('-inf')
    # x값을 기준으로 인접한 두 점의 기울기를 모두 구해서 최대 기울기를 찾아주세요.
    for i in range(1, len(sortedPoints)):
        slope = getSlope(sortedPoints[i-1], sortedPoints[i])
        maxSlope = max(maxSlope, slope)
    
    # maxSlope 값을 소수점 4번째 자리에서 반올림해서 반환해 주세요.
    return round(maxSlope, 4)


def main():
    n = int(input())
    
    points = []
    for i in range(n):
        point = [int(x) for x in input().split()]
        points.append(point)
        
    print("%.3lf" % findMaxSlope(points))

if __name__ == "__main__":
    main()



#---미션2 - 컴퓨터 배정---



def maximumPeopleUsage(times):
    result = 0
    
    # 이용 시간을 정렬해요.
    # 종료 시간이 빠른 순서 & 시작 시간이 빠른 순서
    times.sort(key=lambda x: (x[1], x[0]))
    
    # 컴퓨터를 사용할 수 있는 최대 인원수를 계산해 주세요.
    end_time = 0
    for time in times:
        if time[0] >= end_time:
            result += 1
            end_time = time[1]
    
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



#---미션3 - 컴퓨터 배정 심화---



def minimunComputerNeeds(times):
    result = 0
    # 이용 시간을 정렬해요.
    # 종료 시간이 빠른 순서 & 시작 시간이 빠른 순서
    sortedTimes = sorted(times, key = lambda x: (x[1],x[0]))
    
    # 구매해야 하는 컴퓨터의 최소 개수를 계산해 주세요.
    endTime = sortedTimes[0][1]
    for i in range(1, len(sortedTimes)):
        if sortedTimes[i][0] >= endTime:
            endTime = sortedTimes[i][1]
        else:
            result += 1
    return result
    


def main():
    n = int(input())
    times = []
    for _ in range(n):
        time = [int(x) for x in input().split()]
        times.append(time)
    print(minimunComputerNeeds(times))

if __name__ == "__main__":
    main()



#---미션4 - 동전 거스름돈---



def coins(n):
    coin_types = [500, 100, 50, 10]
    result = {}

    for coin in coin_types: #리스트에 있는 동전의 종류를 순서대로 반복
        count = n // coin
        n %= coin
        result[coin] = count

    return result


def main():
    n = int(input())
    cnt = 0
    for value in coins(n).values():
        cnt+=value
    print(cnt)

if __name__ == "__main__":
    main()
