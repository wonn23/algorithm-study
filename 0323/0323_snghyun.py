######## 이승현

#######미션1
def getSlope(point1, point2):
    if point1[0] == point2[0]:
        return 0
    return abs( (point1[1] - point2[1]) / (point1[0] - point2[0]) )


def findMaxSlope(points):
    # x값을 기준으로 점들을 정렬해 주세요.
    points.sort(key = lambda x: x[0])
    
    maxSlope = float("-inf")

    # x값을 기준으로 인접한 두 점의 기울기를 모두 구해서 최대 기울기를 찾아주세요.

    for i in range(len(points)-1):
        maxSlope = max(maxSlope, getSlope(points[i], points[i+1]))

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



####### 미션2
def maximumPeopleUsage(times):
    
    # 종료 시간이 빠른 순서 & 시작 시간이 빠른 순서
    times.sort(key = lambda x: (x[1], x[0]))

    # 컴퓨터를 사용할 수 있는 최대 인원수를 계산해 주세요.
    count = 0  # 학생 수
    last = 0   # 최종 마지막 사용 시간
    for i, j in times:
        if i >= last:
            count += 1
            last = j
    
    return count


def main():
    n = int(input())
    times = []
    for _ in range(n):
        time = [int(x) for x in input().split()]
        times.append(time)
    print(maximumPeopleUsage(times))

if __name__ == "__main__":
    main()



##########미션3
def minimunComputerNeeds(times):
    
    # 종료 시간이 빠른 순서 & 시작 시간이 빠른 순서
    times.sort(key = lambda x: (x[1], x[0]))
    
    # 구매해야 하는 컴퓨터의 최소 개수를 계산해 주세요.
    count = 0   # 사용한 컴퓨터 총 개수

    while(True):
        last = 0     # 최종 마지막 컴퓨터 종료 시간
        rest_times = []     # 선택된 시간표를 제외한 나머지 시간표들이 담긴 리스트 선언
        for i,j in times:
            if i >= last:
                last = j          
            else:
                rest_times.append([i,j])   # 선택되지 않은 시간표들을 따로 모아서 rest_times 리스트에 저장
                
        count += 1   
        times = rest_times
        if(len(times) == 0):   # 만약 rest_times에 속한 요소가 아무것도 없을 경우(= 남은 시간표가 없다), break
            break
            
    return count-1   # 사용해야할 전체 컴퓨터 수가 아닌, 추가로 구매한 컴퓨터 수만 카운트 하면 되기 때문에 -1
    
    

def main():
    n = int(input())
    times = []
    for _ in range(n):
        time = [int(x) for x in input().split()]
        times.append(time)
    print(minimunComputerNeeds(times))

if __name__ == "__main__":
    main()



###### 미션4
def coins(n):
    # 동전 종류가 주어집니다.
    coins = [10, 50, 100, 500] 
    coins.sort(reverse=True) 
    coinCount = 0
    for coin in coins:
        # 각 동전이 사용되는 개수를 저장해 주세요. (힌트: 나눗셈의 몫 활용)
        coinCount = coinCount + (n // coin)
        # 동전으로 거스르고 남은 금액을 갱신해 주세요.
        n = n % coin
        
    return coinCount


def main():
    n = int(input())
    print(coins(n))



if __name__ == "__main__":
    main()
