def minimumRoomNeeded(times):
    # 주어진 식사 시간을 정렬해 주세요.
    sortedTimes = times
    sortedTimes.sort(key = lambda x : (x[1],x[0]))     # 식사 종료 시간 기준 오름차순 정렬
    #print(sortedTimes)
    
    # 최소 식사 방의 개수를 구해주세요.
    rooms = [0]         # 앞 강쥐 식사 종료 시간 담는 배열
    
    for i in range(len(sortedTimes)) :      
        for j in range(len(rooms)) :
            if sortedTimes[i][0] >= rooms[j] :      
                # 다음 강쥐 시작 시간이 앞 강쥐 종료 시간보다 크면 앞 강쥐는 이미 먹고 나갔으니까 들어갈 수 있음
                rooms[j] = sortedTimes[i][1]
                # 다음 강쥐 들어갔으니까 들어간 애 종료 시간 넣어줌
                break
        else : rooms.append(sortedTimes[i][1])      # ...?
        #print('rooms',rooms)
    return len(rooms)


def main():
    N = int(input())
    times = []
    for _ in range(N):
        time = [int(x) for x in input().split()]
        times.append(time)
    print(minimumRoomNeeded(times))


if __name__ == "__main__":
    main()