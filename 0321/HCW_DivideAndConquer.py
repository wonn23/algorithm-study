### 미션1 - 최댓값 찾기 ###

def maxOfArray(arr):
    if len(arr) == 1:
        # 탈출 조건을 작성해 주세요.
        return arr
    
    # 핵심 기능을 작성해 주세요.
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    leftMax = maxOfArray(left)
    rightMax = maxOfArray(right)

    if leftMax < rightMax:
        return rightMax
    else:
        return leftMax
    
    

def main():
    arr = [int(x) for x in input().split()]
    print(list(maxOfArray(arr))[0])


if __name__ == "__main__":
    main()
    

### 미션2 - 최솟값 찾기 ###

def minOfArray(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    leftMin = minOfArray(left)
    rightMin = minOfArray(right)

    if leftMin < rightMin:
        return leftMin
    else:
        return rightMin

def main():
    arr = [int(x) for x in input().split()]
    print(list(minOfArray(arr))[0])


if __name__ == "__main__":
    main()
    

### 미션 3 - 퀵 정렬 알고리즘 ###
    
def quickSort(arr):
    if len(arr) <= 1:
        return arr

    
    pivot = arr.pop(0)
    left = [x for x in arr if pivot >= x]
    right = [x for x in arr if pivot < x]
    
    return quickSort(left) + [pivot] + quickSort(right) 


def main():
    arr = [int(x) for x in input().split()]
    print(quickSort(arr))


if __name__ == "__main__":
    main()


### 미션 4 - 합병 정렬 알고리즘

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        SortedLeft = mergeSort(left)
        SortedRight = mergeSort(right)
    return merge(SortedLeft, SortedRight)


def merge(left, right):
    S = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            S.append(left[i])
            i+=1
        else:
            S.append(right[j])
            j+=1
    if i < len(left):
        S += left[i:]
    else:
        S += right[j:]
    return S


def main():
    arr = [int(x) for x in input().split()]
    print(mergeSort(arr))


if __name__ == "__main__":
    main()
    

### 미션5 - 이진 탐색 ###

def binarySearch(arr, target):
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
        newArr = arr[:mid]
    
    # 알맞은 매개변수와 함께 재귀 함수를 호출해 주세요.
    return binarySearch(newArr, target)


def main():
    arr    = [int(x) for x in input().split()]
    target = int(input())
    
    print(binarySearch(arr, target))


if __name__ == "__main__":
    main()
