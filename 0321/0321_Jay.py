############## 1번문제 최댓값찾기
def maxOfArray(arr):
    if len(arr) == 1:
        # 탈출 조건을 작성해 주세요.
        return arr
    
    # 핵심 기능을 작성해 주세요.
    mid = len(arr) // 2
    leftMax = max(arr[:mid])
    rightMax = max(arr[mid:])
    
    # leftMax, rightMax를 비교해서 더 큰 값을 반환해 주세요.
    return max(leftMax,rightMax)


def main():
    arr = [int(x) for x in input().split()]
    print(maxOfArray(arr))


if __name__ == "__main__":
    main()

################ 2번문제 최솟값 찾기
def minOfArray(arr):
    if len(arr) == 1: return arr

    mid = len(arr) // 2
    leftMin = min(arr[:mid])
    rightMin = min(arr[mid:])
    
    # leftMax, rightMax를 비교해서 더 큰 값을 반환해 주세요.
    return min(leftMin,rightMin)

def main():
    arr = [int(x) for x in input().split()]
    print(minOfArray(arr))


if __name__ == "__main__":
    main()

################ 3번문제 퀵 알고리즘
def quickSort(arr):

    if len(arr) <= 1: return arr

    pivot = arr[0]
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]

    return quickSort(left) + [pivot] + quickSort(right)


def main():
    arr = [int(x) for x in input().split()]
    print(quickSort(arr))


if __name__ == "__main__":
    main()

################ 4번문제 합병 정렬
def mergeSort(arr):
    if len(arr) <= 1: return arr
    
    # 핵심 기능을 작성해 주세요.
    mid   = len(arr)//2
    left  = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    return merge(left,right)


def merge(l,r):
    sortedList = []
    i = 0
    j = 0

    while i < len(l) and j < len(r):
        if l[0] <= r[0]:
            sortedList.append(l.pop(0))
        else:
            sortedList.append(r.pop(0))

    if i < len(l):
        sortedList += l
    elif j < len(r):
        sortedList += r

    return sortedList
    
def main():
    arr = [int(x) for x in input().split()]
    print(mergeSort(arr))


if __name__ == "__main__":
    main()

################# 5번 문제 이진탐색
def binarySearch(arr, target):
    if len(arr) == 0:
        # 탈출 조건을 작성해 주세요.
        return False
    
    # 핵심 기능을 작성해 주세요.
    mid = len(arr) // 2
    
    if arr[mid] == target:
        # arr[mid] 값이 target인 경우 무엇을 해야할까요?
        return True
        
    elif arr[mid] < target:
        # arr[mid] 값이 target보다 작은 경우, newArr를 새롭게 설정해 주세요.
        newArr = arr[mid + 1:]
    else:
        # arr[mid] 값이 target보다 큰 경우, newArr를 새롭게 설정해 주세요.
        newArr = arr[:mid]
    
    # 알맞은 매개변수와 함께 재귀 함수를 호출해 주세요.
    return binarySearch(newArr,target)


def main():
    arr    = [int(x) for x in input().split()]
    target = int(input())
    
    print(binarySearch(arr, target))


if __name__ == "__main__":
    main()
