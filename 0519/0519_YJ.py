#k번째 수
def solution(array, commands):
    answer = []
    for i in commands:
        newarray=array[i[0]-1:i[1]]
        newarray.sort()
        answer.append(newarray[i[2]-1])

    return answer

#가장 큰 수
#시간초과~
import itertools
def solution(numbers):
    answer = ''
    joinlist=[]
    p = itertools.permutations(numbers,len(numbers))
    for i in list(p):
        joinp=''.join(map(str,list(i)))
        joinlist.append(joinp)
    answer=str(max(map(int,joinlist)))
    return answer