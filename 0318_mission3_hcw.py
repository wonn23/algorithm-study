def powerSet(s): # 14번 줄에 s는 리스트 형태로 들어올 것이란 것을 알 수 있다.
    powerset = []
    x = len(s) # s의 원소의 개수
    for i in range(1 << x): # 비트연산자 '1 << x'는 1을 x만큼 비트를 왼쪽으로 이동시킨다는 뜻이다. 결과적으로 2**x이고 부분집합의 개수를 뜻한다.
        powerset.append([s[j] for j in range(x) if (i & (1 << j))]) # 리스트 함축을 통해 powerset은 리스트를 원소로 가진 리스트인 것이다.
# powerset 함수에 append는 8번 시행되는 것이고 리스트 함축의 원소는 [1,2,3] 중에서 선택되는 것이다.
    return powerset


def minimumDifference(arr):
    if len(arr) == 0:
        return 0
    
    # 주어진 리스트를 분할하는 가능한 모든 조합을 구해요.
    combinations = powerSet(arr) # [[],[1],[2],[3],[1,2],[2,3],[1,3],[1,2,3]]
    
    # 주어진 리스트의 모든 원소들의 합을 구해요.
    wholeSum = sum(arr) # sum([1,2,3]) = 6
    
    # A그룹과 B그룹의 차이 최솟값을 초기화해요.
    # 최솟값은 아무리 커도 리스트 내 최댓값을 넘지 않으니, 리스트 내 최댓값으로 초기화해요.
    minimumAB = max(arr) # max([1,2,3]) = 3
    
    # 반복문을 통해 모든 조합을 탐색하여 그룹의 차이를 구해주세요.
    for i in range(len(combinations)):
        min_sum = abs(sum(combinations[i]) - sum(combinations[len(combinations)-1-i]))
        if minimumAB > min_sum:
            minimumAB = min_sum
    
    return minimumAB


def main():
    arr = [int(x) for x in input().split()]
    print(minimumDifference(arr))

if __name__ == "__main__":
    main()
