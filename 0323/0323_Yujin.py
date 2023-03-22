#############1번.가장 큰 기울기 찾기###############

#이문제는 막상 제출하면 60점 나오는데 이유를 같이.. 찾아주세요...

def getSlope(point1, point2):
    if point1[0] == point2[0]:
        return 0
    return abs( (point1[1] - point2[1]) / (point1[0] - point2[0]) )


def findMaxSlope(points):
    # x값을 기준으로 점들을 정렬해 주세요.
    sortedPoints = sorted(points, key=lambda x : x[0])
    print(sortedPoints)
    maxSlope = float('-inf')
    # x값을 기준으로 인접한 두 점의 기울기를 모두 구해서 최대 기울기를 찾아주세요.
    # maxSlope 값을 소수점 4번째 자리에서 반올림해서 반환해 주세요.
    for i in range(len(sortedPoints)):
        for j in range(i+1,len(sortedPoints)): 
            print(i,j,sortedPoints[i],sortedPoints[j])
            slope = getSlope(sortedPoints[i],sortedPoints[j])
            maxSlope = round(max(maxSlope,slope),3)
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







######################2.컴퓨터 배정#####################
def maximumPeopleUsage(times):
    result = 1
    
    # 이용 시간을 정렬해요.
    # 종료 시간이 빠른 순서 & 시작 시간이 빠른 순서
    times.sort(key=lambda x: (x[1], x[0]))
    # 컴퓨터를 사용할 수 있는 최대 인원수를 계산해 주세요.

    rightvalue=times[0][1]
    for i in range(1,len(times)):
        if times[i][0] >= rightvalue: 
            result += 1
            rightvalue = times[i][1]
    
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








##################3.컴퓨터 배정 심화####################

#이 문제는 80점 나오는데.. 이것도.. 이유를 같이 찾아주세요..

def minimunComputerNeeds(times):
    result = 1
    # 이용 시간을 정렬해요.
    # 종료 시간이 빠른 순서 & 시작 시간이 빠른 순서
    sortedTimes = sorted(times, key = lambda x: (x[1],x[0]))
    print(sortedTimes)
    
    # 구매해야 하는 컴퓨터의 최소 개수를 계산해 주세요.
    rightvalue=sortedTimes[0][1]
    for i in range(1,len(times)):
        if sortedTimes[i][0] >= rightvalue: 
            result += 1
            rightvalue = sortedTimes[i][1]
    result=len(sortedTimes)-result
    
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






################4.동전 거스름돈######################
def coins(n):
    coinslist=[10,50,100,500]
    coinsdic={}
    coinslist.sort(reverse=True)
    for i in coinslist:
        coinsdic[i]=n//i
        n=n%i

    return coinsdic


def main():
    n = int(input())
    cnt = 0
    for value in coins(n).values():
        cnt+=value
    print(cnt)

if __name__ == "__main__":
    main()
