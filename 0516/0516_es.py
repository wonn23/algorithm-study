#0516 스터디 - 백준 [스택, 큐]

###### 같은 숫자는 시렁~~ ###
#1 처음 아이디어
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    
    return answer

#2 인덱싱 안하고 de변수와 비교. 시간 젤 짧음
def solution(arr):
	answer=[]
	de = None
	for elem in arr:
		if elem != de:
			answer.append(elem)
			de = elem
	return answer

#3 스택 써보려고 굳이 append하고 pop함
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        answer.append(arr[i])
        if arr[i] == arr[i-1]:
            answer.pop()
    return answer


###### 올바른 괄호 ###
def solution(s):
    gwal = [] #괄. 스택!

    for c in s:       
        if c == '(' :
            gwal.append(c)      #'('이면 스택에 추가
        else:
            if '(' in gwal:     #')'이고, '('이 스택에 있다면 가장 마지막 '(' 제거
                gwal.pop()
            else:
                return False    #')'이고, '(' 스택에 없으면 False

    if gwal:            #for문 다 돌았는데 아직도 괄 안비었으면 False
        return False
    
    return True


###### 기능 개발 ###
#1 처음 아이디어. 냅다 작업일 계산
import math;


def solution(progresses, speeds):
    Q = []
    answer = []
    release = 0
    
    for i in range(len(speeds)):
        Q.append(math.ceil((100-progresses[i]) / speeds[i])) # (100 - 작업량) / 하루 작업량 = 작업일
        
    #print(Q)
    for j in range(len(Q)):
        if Q[j] > Q[release]:
            answer.append(j-release) #앞에 애들 동시 출시
            release = j
    
    answer.append(len(Q)-release) #남은 애들 출시
        
        
    return answer


#2 큐 쓰고 싶어서 써봤다........후회..
def solution(progresses, speeds):
    answer = []
    cnt = 0
    day = 0
    
    while len(progresses)>0: #progresses가 남아있을 때까지
        if (progresses[0] + day*speeds[0] >= 100): #작업 완. 배포 가능
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1 #cnt: 같이 배포할 기능 모집
        else:
            if cnt > 0: #앞에 애 준비돼서 넘어왔는데 뒤에 애는 준비 안됐을 때
                answer.append(cnt) #앞에 애들 먼저 배포시켜줌
                cnt = 0 #앞 애들 배포 됐으니까 cnt 초기화
            day += 1 #하루가 가네요..
    answer.append(cnt) #마지막 애 작업 끝나면 else문 들어갈 일이 없으니까 밖에서 append해줌
                
    return answer


##### 프로세스 ###
def solution(priorities, location):
    cnt=0
    
    while len(priorities)>0:
        maxP = max(priorities)
        p = priorities.pop(0) #pop(0) -> 큐
        location -= 1  #앞에서 빠지면 location인덱스도 줄어듦
        
        if p == maxP:
            cnt+=1
            if location < 0: 
                break       #p가 location이었다면 break
        else:
            priorities.append(p)
            if location<0: #앞에서 빠졌는데 우선순위 1등 아니면 맨 뒤로 가니까
                location = len(priorities) -1       
    return cnt