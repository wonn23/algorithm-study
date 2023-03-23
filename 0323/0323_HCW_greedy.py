# 그리디 알고리즘

### 미션1 - 가장 큰 기울기 찾기 ###

def getSlope(point1, point2):
    if point1[0] == point2[0]:
        return 0
    return abs( (point1[1] - point2[1]) / (point1[0] - point2[0]) )


def findMaxSlope(points):
    # x값을 기준으로 점들을 정렬해 주세요.
    sortedPoints = sorted(points, key = lambda x : x[0])
    
    maxSlope = float('-inf')
    # x값을 기준으로 인접한 두 점의 기울기를 모두 구해서 최대 기울기를 찾아주세요.
    
    for i in range(len(sortedPoints)):
        for j in range(i+1,len(sortedPoints)):
            if maxSlope < getSlope(sortedPoints[i],sortedPoints[j]):
                maxSlope = getSlope(sortedPoints[i],sortedPoints[j])

    # maxSlope 값을 소수점 4번째 자리에서 반올림해서 반환해 주세요.
    return round(maxSlope,4)


def main():
    n = int(input())
    
    points = []
    for i in range(n):
        point = [int(x) for x in input().split()]
        points.append(point)
        
    print("%.3lf" % findMaxSlope(points))

if __name__ == "__main__":
    main()



### 미션2 - 컴퓨터 배정 ###

def maximumPeopleUsage(times):
    result = 0
    
    # 이용 시간을 정렬해요.
    # 종료 시간이 빠른 순서 & 시작 시간이 빠른 순서. 종료시간 순서로 오름 차순 한 후 시작시간 순서로 오름차순 정렬한다.
    times.sort(key=lambda x: (x[1], x[0]))
    
    # 컴퓨터를 사용할 수 있는 최대 인원수를 계산해 주세요.
    person = [0]

    for com in times:
        if not person:
            person.append(com[1])
        else:
            if com[0] >= person[0]:
                person.pop(0)
                person.append(com[1])
                result += 1
    
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


### 미션3 - 컴퓨터 배정 심화 ###

def minimumComputerNeeds(times):
    result = 1
    
    # 이용 시간을 정렬해요.
    # 종료 시간이 빠른 순서 & 시작 시간이 빠른 순서. 종료시간 순서로 오름 차순 한 후 시작시간 순서로 오름차순 정렬한다.
    times.sort(key=lambda x: (x[1], x[0]))
    
    # 컴퓨터를 사용할 수 있는 최대 인원수를 계산해 주세요.
    person = []

    for com in times:
        if not person:
            person.append(com[1])
        else:
            if com[0] >= person[0]:
                person.pop(0)
                person.append(com[1])
                result += 1
            
    return len(times) - result

def main():
    n = int(input())
    times = []
    for _ in range(n):
        time = [int(x) for x in input().split()]
        times.append(time)
    print(minimumComputerNeeds(times))

if __name__ == "__main__":
    main()

    
### 미션4 동전 거스름돈 ###

def coins(n):
    coins_count = 0
    coins_list = [500,100,50,10]
    
    for i in coins_list:
        if n//i !=0:
            coins_count += n//i
            n -= n//i * i
    return coins_count


def main():
    n = int(input())
    print(coins(n))

if __name__ == "__main__":
    main()
