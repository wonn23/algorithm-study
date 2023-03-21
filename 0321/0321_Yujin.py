#### 1.최댓값 찾기#####
def maxOfArray(arr):
    if len(arr) == 1:
        # 탈출 조건을 작성해 주세요.
        return arr
    
    # 핵심 기능을 작성해 주세요.
    mid = len(arr)//2
    leftMax = maxOfArray(arr[:mid])
    rightMax = maxOfArray(arr[mid:])
    
    # leftMax, rightMax를 비교해서 더 큰 값을 반환해 주세요.
    return max(maxOfArray(leftMax),maxOfArray(rightMax))


def main():
    arr = [int(x) for x in input().split()]

    print(" ".join(str(s) for s in maxOfArray(arr)))

if __name__ == "__main__":
    main()




#### 2. 최솟값 찾기 ####
def minOfArray(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    leftmin=minOfArray(left)
    rightmin=minOfArray(right)

    return min(leftmin,rightmin)

def main():
    arr = [int(x) for x in input().split()]
    # print(''.join(str(i) for i in minOfArray(arr)))
    print(''.join(map(str,minOfArray(arr))))

if __name__ == "__main__":
    main()





#### 3.퀵 정렬 알고리즘####
def quickSort(arr):
    if len(arr)<=1:
        return arr

    pivot=arr[0]
    left=[]
    right=[]

    for i in arr[1:]:
        if i<pivot:
            left.append(i)
        else:
            right.append(i)
    
    quickleft = quickSort(left)
    quickright = quickSort(right)

    return quickleft+[pivot]+quickright

def main():
    arr = [int(x) for x in input().split()]
    print(quickSort(arr))


if __name__ == "__main__":
    main()






#### 4.합병 정렬 알고리즘 ####
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    midleft = arr[:mid]
    midright = arr[mid:]

    mergeleft = mergeSort(midleft)
    mergeright = mergeSort(midright)

    return merge(mergeleft,mergeright)


def merge(left, right):
    mergeList=[]
    i=0
    j=0
    while i<len(left) and j<len(right) :
        if left[i]<right[j]:
            mergeList.append(left[i])
            i+=1

        else:
            mergeList.append(right[j])  
            j+=1
    
    mergeList+=left[i:]
    mergeList+=right[j:]

    return mergeList


def main():
    arr = [int(x) for x in input().split()]
    print(mergeSort(arr))


if __name__ == "__main__":
    main()







#### 5. 이진 탐색####
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
