#### 0404 스터디 - 그래프 알고리즘
##미션1 
def virusDFS(target):
    # 스택 구조를 정의해요.
    stack = []
    
    # 탐색의 시작점 1을 정의해요.
    initialNode = 1
    
    # 0부터 10000까지의 노드에 대한 방문 정보를 담은 리스트를 정의해요.
    visited = [ 0 for i in range(0, 10001)]
    
    # 첫 번째 방문할 노드는 1이지요. 노드 1에 대한 방문 정보를 갱신해 주세요.
    visited[1] = initialNode
    
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
            adjacentNodes = [node for node in adjacentNodes if node <= 10000]
            for node in adjacentNodes:
                if visited[node] == 0:
                    visited[node] = visitedNode
                    stack.append(node)
    return False
            

def main():
    target = int(input())
    
    print(virusDFS(target))


if __name__ == "__main__":
    main()



##미션2 이상한 소문
import queue

def gossipCounts(n, graph):
    # 소문이 퍼진 횟수를 저장할 변수예요.
    count = 0

    Q = queue.Queue()
    visited = [False] * (n+1)
    visited[1] = True
    Q.put(1)
    
    # 1번 노드와 연결된 노드가 없는 경우 예외 처리
    if not graph[1]:
        return count

    while not Q.empty():
        node = Q.get()
        count += 1
        for otherStudent in graph[node]:
            if not visited[otherStudent]:
                visited[otherStudent] = True
                Q.put(otherStudent)
    
    return count-1


# 입력받은 pairs를 그래프 자료구조로 사용할 수 있도록 바꿔주는 함수에요.
def getGraph(n, pairs):
    graph = [[] for i in range(n+1)]
    m_edges = len(pairs)
    for pair in pairs :
        graph[pair[0]].append(pair[1])
        graph[pair[1]].append(pair[0])
    return graph


def main():
    n_nodes = int(input())
    m_edges = int(input())

    myInput = []

    for i in range(m_edges) :
        line = [int(x) for x in input().split()]
        myInput.append(line)

    print(gossipCounts(n_nodes, getGraph(n_nodes, myInput)))


if __name__ == "__main__":
    main()


##미션3 유치원 소풍
def getAdjacentNodes(studentsMap, i, j):
    adjacentNodes = []
    # studentMap에서 상하좌우의 인접 노드를 구해 주세요.
    # i, j에서 상하좌우에 대해 탐색
    # 좌표 범위 내에 있고, 학생이 있다면 1, 인접 노드 리스트에 추가
    n = len(studentsMap)
    #print(studentsMap)

    if i >= 1 and studentsMap[i-1][j] == 1:
        adjacentNodes.append((i-1, j))
    if i < n-1 and studentsMap[i+1][j] == 1:
        adjacentNodes.append((i+1, j))
    if j >= 1 and studentsMap[i][j-1] == 1:
        adjacentNodes.append((i, j-1))
    if j < n-1 and studentsMap[i][j+1] == 1:
        adjacentNodes.append((i, j+1))
    
    
    return adjacentNodes

def picnicCounts(n, studentsMap):
    classCounts = 0  # 반 전체 개수
    studentCountsForEachClass = {} # 각 반에 속한 학생 개수
    
    # 모든 노드에 대한 방문 정보를 담은 리스트를 정의해요.
    visited = [[False for i in range(n)] for j in range(n)] 
    
    for i in range(n):
        for j in range(n):
            # 방문하지 않았고 (i, j) 위치에 학생이 있으면 반을 하나 새로 만든다! ...
            if not visited[i][j] and studentsMap[i][j] != 0:
                classCounts += 1
                studentCountsForEachClass[classCounts] = 0
                
                # 스택 구조를 정의해요.
                stack = []
                # (i, j) 좌표에 대한 방문이 완료되었으니 방문 정보를 갱신해 주세요.
                visited[i][j] = True                
                # 방문이 완료되었으니, 노드를 스택에 추가해 주세요.
                stack.append((i, j))         
                
                # 각 반에 속한 학생의 수를 갱신해 주세요.
                studentCountsForEachClass[classCounts] += 1
                
                # 스택이 비어있지 않은 경우에만 반복문을 돌도록 조건을 설정해 주세요.
                while stack:
                    # 방문한 노드를 꺼내 주세요.
                    visitedNode = stack.pop()
                    
                    # 인접 노드를 계산해요.
                    adjacentNodes = getAdjacentNodes(studentsMap, visitedNode[0], visitedNode[1])
                    
                    # 방문하지 않은 인접 노드를 방문해 주세요.
                    for node in adjacentNodes:
                        if not visited[node[0]][node[1]]:
                            visited[node[0]][node[1]] = True
                            stack.append(node)
                            studentCountsForEachClass[classCounts]+= 1
                    
                    
    result = str(classCounts)
    sortedStudentCounts = sorted(studentCountsForEachClass.values())
    for i in range(classCounts):
        result += "\n"
        result += str(sortedStudentCounts[i])
    return result


def main():
    n = int(input())
    lines = []
    # 하...... 제대로 넣어 주시길...... 문의 넣었다
    for _ in range(n):
        line = list(input())
        line = [int(x) for x in line]
        lines.append(line)
    
    print(picnicCounts(n, lines))


if __name__ == "__main__":
    main()
