#자소서 쓰느라 시간이 없...ㅜ_ㅜ
#절대 노느라 그런 것도 맞음.

#최직각
def solution(sizes):
    answer = 0
    w = 0
    h = 0
    
    for i in sizes:
        if i[0] < i[1]: 
            i[0], i[1] = i[1], i[0]
        if i[0] > w:  
            w = i[0]
            
        if i[1] > h: 
            h = i[1]
    
    answer = w * h  
    return answer

#모의고사
#푸는 방법 거의 원시인
def solution(answers):
    answer = []
    s1=[1,2,3,4,5]*2000
    s2=[2,1,2,3,2,4,2,5]*1300
    s3=[3,3,1,1,2,2,4,4,5,5]*1000
    answer1=0
    answer2=0
    answer3=0
    for i in range(len(answers)):
        if answers[i]==s1[i]:
            answer1+=1
        if answers[i]==s2[i]:
            answer2+=1
        if answers[i]==s3[i]:
            answer3+=1

    if answer1>=answer2 and answer1>=answer3:
        answer.append(1)
    if answer2>=answer1 and answer2>=answer3:
        answer.append(2)
    if answer3>=answer1 and answer3>=answer2:
        answer.append(3)
    return answer
