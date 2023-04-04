###### 1. 바이러스 ######

def virusDFS(target):
    # 스택 구조를 정의해요.
    stack = []
    
    # 탐색의 시작점 1을 정의해요.
    initialNode = 1
    
    # 0부터 10000까지의 노드에 대한 방문 정보를 담은 리스트를 정의해요.
    visited = [ 0 for i in range(0, 10001)]
    
    # 첫 번째 방문할 노드는 1이지요. 노드 1에 대한 방문 정보를 갱신해 주세요.
    visited[1]=1
    
    # 방문이 완료되었으니, 노드 1을 스택에 추가해 주세요. append 메서드를 사용해 보세요.
    stack.append(visited[1])
    
    # 스택이 비어있지 않은 경우에만 반복문을 돌도록 조건을 설정해 주세요.
    while stack:
        # 방문한 노드를 꺼내 주세요.
        visitedNode = stack.pop()
        
        # 방문한 노드가 타겟 노드라면 탐색은 종료되고 True을 반환해요.
        if visitedNode == target:
            return True
            
        else:
        # 인접 노드를 계산해요.
            adjacentNodes = [visitedNode*2, visitedNode//3]
            
            # 방문하지 않은 인접 노드를 방문해 주세요.
            for node in adjacentNodes:
                    if node <= 10000 :
                        if visited[node] == 0:
                            visited[node] = visited[visitedNode] + 1 
                            stack.append(node)
            
    return False


def main():
    target = int(input())
    
    print(virusDFS(target))


if __name__ == "__main__":
    main()








###### 3. 유치원 소풍 ######

def getAdjacentNodes(studentsMap, i, j):
    adjacentNodes = []
    # studentMap에서 상하좌우의 인접 노드를 구해 주세요.
    # [0, 1, 1, 0, 1, 0, 0]
    # [0, 1, 1, 0, 1, 0, 1]
    # [1, 1, 1, 0, 1, 0, 1]
    # [0, 0, 0, 0, 1, 1, 1]
    # [0, 1, 0, 0, 0, 0, 0]  2차원 배열로 보는 studentsMap,,
    # [0, 1, 1, 1, 1, 1, 0]
    # [0, 1, 1, 1, 0, 0, 0]
    #여기서 i는 방문한 node의 y값 , j는 x값

    # 위쪽 노드
    if i > 0 and studentsMap[i-1][j] == 1: #i가 0보다 크고 저 map에서 visitednode(=(i,j))의 바로 위쪽 값이 1이어야 true
        adjacentNodes.append((i-1, j)) # 위쪽값을 배열에 append
        
    # 아래쪽 노드
    if i < len(studentsMap) - 1 and studentsMap[i+1][j] == 1: #i가 map의 길이 보다 작고(그래야 아래가 있음) 아래쪽 값이 1이면 true
        adjacentNodes.append((i+1, j)) # 아래쪽 값을 배열에 append
        
    # 왼쪽 노드
    if j > 0 and studentsMap[i][j-1] == 1: #j가 0보다 크고(그래야 왼쪽이 존재) 왼쪽값이 1이면 true
        adjacentNodes.append((i, j-1)) #왼쪽 값을 append
        
    # 오른쪽 노드
    if j < len(studentsMap[i]) - 1 and studentsMap[i][j+1] == 1: #j가 map의 좌우길이보다 작고 오른쪽 값이 1이면 true
        adjacentNodes.append((i, j+1)) #오른쪽 값을 append


    #getAdjacentNodes(studentsMap, 1, 1)를 호출시 adjacentNodes의 값은 [(0, 1), (2, 1),(1, 2)]
    return adjacentNodes

def picnicCounts(n, studentsMap):
    classCounts = 0  # 반 전체 개수
    studentCountsForEachClass = {} # 각 반에 속한 학생 개수
    
    # 모든 노드에 대한 방문 정보를 담은 리스트를 정의해요.
    visited = [[False for i in range(n)] for j in range(n)] 
    #  [False, False, False, False, False, False, False]
    #  [False, False, False, False, False, False, False] 
    #  [False, False, False, False, False, False, False]
    #  [False, False, False, False, False, False, False]
    #  [False, False, False, False, False, False, False]
    #  [False, False, False, False, False, False, False]
    #  [False, False, False, False, False, False, False]

    for i in range(n): #행
        for j in range(n): #열
            if not visited[i][j] and studentsMap[i][j] != 0: #visited라는 불린값들의 map에서 false이고(방문을 안 했다는 뜻) 그 자리의 studentmap이 0이 아니면 true
                classCounts += 1 #반을 의미(1반,2반,3반으로 생각하는 게 편함)
                studentCountsForEachClass[classCounts] = 0 #반 개수 dic{1:0}
                # 스택 구조를 정의해요.
                stack = []
                # (i, j) 좌표에 대한 방문이 완료되었으니 방문 정보를 갱신해 주세요.
                visited[i][j]=True
                
                # 방문이 완료되었으니, 노드를 스택에 추가해 주세요.
                stack.append((i, j)) #(ex.[(0,1)])
                
                # 각 반에 속한 학생의 수를 갱신해 주세요.
                studentCountsForEachClass[classCounts] += studentsMap[i][j] #{1:1}
                
                # 스택이 비어있지 않은 경우에만 반복문을 돌도록 조건을 설정해 주세요.
                while stack:
                    # 방문한 노드를 꺼내 주세요.
                    visitedNode = stack.pop()
                    #visitedNode는 (y,x)(<=튜플)라고 생각하면 됨 ([(a,b),(c,d),..,(y,x)]인 stack에서 pop한 값)

                    # 인접 노드를 계산해요.
                    adjacentNodes = getAdjacentNodes(studentsMap, visitedNode[0], visitedNode[1])
                                                                     # (y.)            (x)
                    # 방문하지 않은 인접 노드를 방문해 주세요.
                    for node in adjacentNodes: #인접노드 (ex.[(0, 1), (2, 1),(1, 0), (1, 2)])
                        if not visited[node[0]][node[1]]: #그 불린값 map에서 저 노드들 중 방문 안 한 곳(false인 곳)
                            visited[node[0]][node[1]] = True # 방문 완료로 바꿔주깅
                            stack.append(node) # stack에다가 그 완료한 노드 추가
                            studentCountsForEachClass[classCounts] += 1 #방문 완료했으니 그 반의 학생 수 +1 (애초에 위~~~의 if문에서 0은 걸렀으므로 무조건 학생 수 +1 하면 됨)
                            # {1: 7, 2: 8, 3: 9}

    result = str(classCounts) #3
    sortedStudentCounts = sorted(studentCountsForEachClass.values()) #[7, 8, 9]
    for i in range(classCounts):
        result += "\n"
        result += str(sortedStudentCounts[i])
    return result


def main():
    n = int(input())
    lines = []
    for _ in range(n):
        line = list(input())
        line = [int(x) for x in line]
        lines.append(line)
    
    print(picnicCounts(n, lines))


if __name__ == "__main__":
    main()






