#### 0321 스터디 - 알고리즘 스타 I - 분할 정복법 ####
#### 미션1 - 최댓값 찾기 ####

def maxOfArray(arr):
    if len(arr) == 1:
        # 탈출 조건을 작성해 주세요.
        return arr[0]
    
    # 핵심 기능을 작성해 주세요.
    mid = len(arr)//2
    leftMax = arr[0:mid]
    rightMax = arr[mid:]
    
    # leftMax, rightMax를 비교해서 더 큰 값을 반환해 주세요.
    if max(leftMax) > max(rightMax):
        return maxOfArray(leftMax)
    else:
        return maxOfArray(rightMax)

# 여기서 split(' ') 썼다가 케이스 다 만점 안 나옴..
# 근데 왜? 인풋을 공백 기준으로 쪼개는 거 아닌가요? 황당하네
def main():
    arr = [int(x) for x in input().split()]
    print(maxOfArray(arr))


if __name__ == "__main__":
    main()


#### 미션2 - 최솟값 찾기 ####

def minOfArray(arr):
    if len(arr) == 1:
        return arr[0]

    mid = len(arr)//2
    leftMin = arr[0:mid]
    rightMin = arr[mid:]

    if min(leftMin) < min(rightMin):
        return minOfArray(leftMin)
    else:
        return minOfArray(rightMin)


def main():
    arr = [int(x) for x in input().split()]
    print(minOfArray(arr))


if __name__ == "__main__":
    main()



#### 미션3 - 퀵 정렬 알고리즘 ####
def quickSort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0] #기준값이 되는 배열의 첫 번째 값
    rest = arr[1:] #나머지 비교할 값을 나타내는 배열

    left = [x for x in rest if x <= pivot] #pivot보다 작거나 같은 값 넣기
    right = [x for x in rest if x > pivot] #pivot보다 큰 값 넣기

    return quickSort(left) + [pivot] + quickSort(right)


def main():
    arr = [int(x) for x in input().split()]
    print(quickSort(arr))


if __name__ == "__main__":
    main()


#### 미션4 - 합병 정렬 알고리즘 ####
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    sortedLeft = mergeSort(left)
    sortedRight = mergeSort(right)

    return merge(sortedLeft, sortedRight)


def merge(left, right):
    i = 0
    j =0
    sortedList = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedList.append(left[i])
            i+=1
        else:
            sortedList.append(right[j])
            j+=1

    sortedList += left[i:]
    sortedList += right[j:]

    
    return sortedList


def main():
    arr = [int(x) for x in input().split()]
    print(mergeSort(arr))


if __name__ == "__main__":
    main()


#### 미션5 - 이진 탐색 ####
def binarySearch(arr, target):

    ## 얘는 입력이 무조건 오름차순으로 정렬되어 있는 건가??
    if len(arr) == 0:
        # 탈출 조건을 작성해 주세요.
        return False
    
    # 핵심 기능을 작성해 주세요.
    mid = len(arr) // 2
    
    if arr[mid] == target:
        # arr[mid] 값이 target인 경우 무엇을 해야할까요?
        return True
        
    if arr[mid] < target:
        # arr[mid] 값이 target보다 작은 경우, newArr를 새롭게 설정해 주세요.
        newArr = arr[mid+1:]
    else:
        # arr[mid] 값이 target보다 큰 경우, newArr를 새롭게 설정해 주세요.
        newArr = arr[0:mid]
    
    # 알맞은 매개변수와 함께 재귀 함수를 호출해 주세요.
    return binarySearch(newArr, target)


def main():
    arr    = [int(x) for x in input().split()]
    target = int(input())
    
    print(binarySearch(arr, target))


if __name__ == "__main__":
    main()
