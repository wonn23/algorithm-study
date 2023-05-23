################## 피로도
import itertools

def solution(k, dungeons):
    permutation_list = list(itertools.permutations(dungeons))
    
    answer = []
    for p in permutation_list:
        total = 0
        k_copy = k
        for i, j in p:
            if i > k_copy:                
                break
            else:
                k_copy = k_copy-j
                total += 1
                
        answer.append(total)

    return max(answer)



############### 최소 직사각형
def solution(sizes):
    
    allWidth = []
    allHeight = []
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
        
        allWidth.append(size[0])
        allHeight.append(size[1])

    return max(allWidth) * max(allHeight)



#################### 모의고사
def solution(answers):
    answer = [0 for i in range(3)]

    man1 = [1,2,3,4,5]
    man2 = [2,1,2,3,2,4,2,5]
    man3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        ans = answers[i]
        if(man1[i%len(man1)] == ans):
            answer[0] += 1
        if(man2[i%len(man2)] == ans):
            answer[1] += 1
        if(man3[i%len(man3)] == ans):
            answer[2] += 1     
    
    result = []
    for i in range(len(answer)):
        if(answer[i] == max(answer)):
            result.append(i+1)
    
    return sorted(result)
