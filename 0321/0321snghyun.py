############## 이승현

###미션1
def maxOfArray(arr):
    if len(arr) == 1:
        # 탈출 조건을 작성해 주세요.
        return arr
    
    # 핵심 기능을 작성해 주세요.
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left.sort()
    right.sort()
    
    # leftMax, rightMax를 비교해서 더 큰 값을 반환해 주세요.
    return left[-1] if left[-1]>=right[-1] else right[-1]


def main():
    arr = [int(x) for x in input().split()]
    print(maxOfArray(arr))


if __name__ == "__main__":
    main()


#### 미션2
def minOfArray(arr):
    if len(arr) == 1:
        # 탈출 조건을 작성해 주세요.
        return arr
    
    # 핵심 기능을 작성해 주세요.
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left.sort()
    right.sort()
    
    # leftMax, rightMax를 비교해서 더 큰 값을 반환해 주세요.
    return left[0] if left[0] <= right[0] else right[0]


def main():
    arr = [int(x) for x in input().split()]
    print(minOfArray(arr))


if __name__ == "__main__":
    main()


### 미션3
def quickSort(arr):
    
    if len(arr) <= 1:  # len(arr) == 1로 했을 때는 오류가 나는 이유: len(arr) == 0 인 경우, pop할 요소가 없기 때문
        return arr

    else:
        pivot = arr.pop(0)

        left_group = list(filter(lambda x: x < pivot, arr))
        right_group = list(filter(lambda x: x >= pivot, arr))

        return quickSort(left_group) + [pivot] + quickSort(right_group)

def main():
    arr = [int(x) for x in input().split()]
    print(quickSort(arr))


if __name__ == "__main__":
    main()



### 미션4
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid   = len(arr) // 2
    left  = arr[:mid]
    right = arr[mid:]
    
    sortedLeft  = mergeSort(left)
    sortedRight = mergeSort(right)
    
    return merge(sortedLeft, sortedRight)


# 합병 정렬 알고리즘에서 리스트를 정렬하는 함수예요.
def merge(left, right):
    i = 0  # left 리스트의 인덱스 처음부터
    j = 0  # right 리스트의 인덱스 처음부터
    sortedList = []
    
    while (i < len(left)) and (j<len(right)):
        if left[i] < right[j]:
            sortedList.append(left[i])
            i += 1
        else:
            sortedList.append(right[j])
            j += 1
    
    # 한쪽만 남아 있는 리스트 처리
    while i < len(left):            # left 리스트가 아직 남았을 경우
        sortedList.append(left[i])
        i += 1
    
    while j < len(right):           # right 리스트가 아직 남았을 경우
        sortedList.append(right[j])
        j += 1
    
    return sortedList

def main():
    arr = [int(x) for x in input().split()]
    print(mergeSort(arr))
    
if __name__ == "__main__":
    main()
    
    
### 미션5
def binarySearch(arr, target):
    arr.sort()

    if len(arr) == 0:          # arr안에 아무것도 없음(target과 비교할 요소가 없음) -> False
        return False
    else:                      # arr안에 요소가 하나라도 있음
        mid = len(arr) // 2    
        
        if arr[mid] == target:   
            return True           
            
        elif arr[mid] < target:
            newArr = arr[mid+1:len(arr)]

        else:
            newArr = arr[:mid]
        
        return binarySearch(newArr,target)  # 가운데에 위치한 요소와 target값이 일치할 때까지 계속 재귀함수 돌리기


def main():
    arr = [int(x) for x in input().split()]
    target = int(input())
    
    print(binarySearch(arr, target))


if __name__ == "__main__":
    main()
