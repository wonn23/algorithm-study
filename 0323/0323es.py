# 이은석_0321 스터디 [탐욕적 기법]

#1 가장 큰 기울기 찾기
def getSlope(point1, point2):
    if point1[0] == point2[0]:
        return 0
    return abs( (point1[1] - point2[1]) / (point1[0] - point2[0]) )


def findMaxSlope(points):
    # x값을 기준으로 점들을 정렬해 주세요.
    points.sort(key = lambda x:x[0])
    sortedPoints = points
    # sortedPoints = sorted(points, key=lambda x: x[0])

    maxSlope = float('-inf')
    # x값을 기준으로 인접한 두 점의 기울기를 모두 구해서 최대 기울기를 찾아주세요.
    for i in range(len(sortedPoints)-1) :
        maxSlope = max(getSlope(sortedPoints[i],sortedPoints[i+1]),maxSlope)

    
    # maxSlope 값을 소수점 4번째 자리에서 반올림해서 반환해 주세요.
    return round(maxSlope,3)


def main():
    n = int(input())
    
    points = []
    for i in range(n):
        point = [int(x) for x in input().split()]
        points.append(point)
        
    print("%.3lf" % findMaxSlope(points))

if __name__ == "__main__":
    main()


#2 컴퓨터 배정
def maximumPeopleUsage(times):
    result = 0
    
    # 이용 시간을 정렬해요.
    # 종료 시간이 빠른 순서 & 시작 시간이 빠른 순서
    times.sort(key=lambda x: (x[1], x[0]))
    #print(times)
    # 컴퓨터를 사용할 수 있는 최대 인원수를 계산해 주세요.
    user = [0]
    for i in range(len(times)) :
        if times[i][0] >= user[-1] :
            user.append(times[i][1])
        
    return len(user)-1


def main():
    n = int(input())
    times = []
    for _ in range(n):
        time = [int(x) for x in input().split()]
        times.append(time)
    print(maximumPeopleUsage(times))

if __name__ == "__main__":
    main()


#3 컴퓨터 배정 심화
# 하아아ㅏ아아아아.......................... 100점 맞고싶다 .. . ..
def minimunComputerNeeds(times):
    result = 0
    # 이용 시간을 정렬해요.
    # 종료 시간이 빠른 순서 & 시작 시간이 빠른 순서
    sortedTimes = sorted(times, key = lambda x: (x[1],x[0]))
    
    
    # 구매해야 하는 컴퓨터의 최소 개수를 계산해 주세요.

    user = [0]
    user1 = []
    for i in range(len(sortedTimes)) :
        if sortedTimes[i][0] >= user[-1] :
            user.append(sortedTimes[i][1])
            user1.append(i)

    computer = [0]
    # computer를 사야되는 사람은 len(sortedTimes) - len(user)
    p = sortedTimes[user1.pop():]
    
    for i in range(len(p)) :
        if p[i][0] >= computer[-1] :
            computer.append(p[i][1])

    return len(computer)-1


def main():
    n = int(input())
    times = []
    for _ in range(n):
        time = [int(x) for x in input().split()]
        times.append(time)
    print(minimunComputerNeeds(times))

if __name__ == "__main__":
    main()


#4 동전 거스름돈
def coins(n):
    coin = [10, 50, 100, 500]
    coin.sort(reverse=True)

    result = []
                    #result = {x: 0 for x in coins}

    for i in coin :
        result.append(n // i)
        n = n % i
                    #result[coin] = coinCount
    return result


def main():
    n = int(input())
    cnt = 0
    for value in coins(n):              #for value in coins(n).values():
        cnt+=value
    print(cnt)

if __name__ == "__main__":
    main()
