# 이은석_0321 스터디 [분할 정복법]

#1. 최댓값 찾기
def maxOfArray(arr):
    if len(arr) <= 1:
        # 탈출 조건을 작성해 주세요.
        return arr[0]
    
    # 핵심 기능을 작성해 주세요.
    mid = len(arr) // 2

    leftMax = maxOfArray(arr[:mid])
    rightMax = maxOfArray(arr[mid:])
    

    # leftMax, rightMax를 비교해서 더 큰 값을 반환해 주세요.
    
    return leftMax if(leftMax > rightMax) else(rightMax)

def main():
    arr = [int(x) for x in input().split()]
    print(maxOfArray(arr))


if __name__ == "__main__":
    main()



#2. 최솟값 찾기
def minOfArray(arr):
    if len(arr)<=1 : 
        return arr[0]

    mid = len(arr) // 2
    leftMin = minOfArray(arr[:mid])
    rightMin = minOfArray(arr[mid:])

    return leftMin if(leftMin < rightMin) else(rightMin)

def main():
    arr = [int(x) for x in input().split()]
    print(minOfArray(arr))


if __name__ == "__main__":
    main()



#3. 퀵 정렬 알고리즘
def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [];
    right = [];
    for i in range(1,len(arr)) :
        if arr[i] < pivot :
            left.append(arr[i])
        elif arr[i] > pivot :
            right.append(arr[i])
        else : 
            left.append(arr[i])

    return quickSort(left) + [pivot] + quickSort(right)


def main():
    arr = [int(x) for x in input().split()]
    print(quickSort(arr))


if __name__ == "__main__":
    main()



#4. 합병 정렬 알고리즘
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    #print(left,right,'a')

    leftMerge = mergeSort(left)
    rightMerge = mergeSort(right)  
    #print(leftMerge,rightMerge,'b')
    
    return merge(leftMerge,rightMerge)


def merge(left, right):
    i=0
    j=0
    sortedList = []
    while i < len(left) and j < len(right) :
        if left[i] < right[j]:
            sortedList.append(left[i])
            i+=1
        else :
            sortedList.append(right[j])
            j+=1
        #print(sortedList,'c')

    #print(i,j,sortedList,'d')
    sortedList += left[i:]
    sortedList += right[j:]

    #print(sortedList,'e')
    return sortedList


def main():
    arr = [int(x) for x in input().split()]
    print(mergeSort(arr))


if __name__ == "__main__":
    main()


#5. 이진탐색
def binarySearch(arr, target):
    if len(arr) <= 1:
        # 탈출 조건을 작성해 주세요.
        return False
    
    # 핵심 기능을 작성해 주세요.
    mid = len(arr) // 2
    
    if arr[mid] == target:
        # arr[mid] 값이 target인 경우 무엇을 해야할까요?
        return True
        
    if arr[mid] < target:
        # arr[mid] 값이 target보다 작은 경우, newArr를 새롭게 설정해 주세요.
        newArr = arr[mid:]
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