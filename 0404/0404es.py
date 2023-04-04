#0404 스터디 그래프 알고리즘_BFS/DFS

#1번 바이러스#####
def virusDFS(target):
    # 스택 구조를 정의해요.
    stack = []
    
    # 탐색의 시작점 1을 정의해요.
    initialNode = 1
    
    # 0부터 10000까지의 노드에 대한 방문 정보를 담은 리스트를 정의해요.
    visited = [ 0 for i in range(0, 10001)]
    
    # 첫 번째 방문할 노드는 1이지요. 노드 1에 대한 방문 정보를 갱신해 주세요.
    # 방문이 완료되었으니, 노드 1을 스택에 추가해 주세요. append 메서드를 사용해 보세요.
    visited[initialNode] = 1
    stack.append(initialNode)
    
    # 스택이 비어있지 않은 경우에만 반복문을 돌도록 조건을 설정해 주세요.
    while stack:
        # 방문한 노드를 꺼내 주세요.
        visitedNode = stack.pop()
        print('방문',visitedNode)
        # 방문한 노드가 타겟 노드라면 탐색은 종료되고 True을 반환해요.
        if visitedNode == target:
            return True
            break
            
        else:
        # 인접 노드를 계산해요.
            adjacentNodes = [visitedNode*2, visitedNode//3]
            print('인접',adjacentNodes)
            # 방문하지 않은 인접 노드를 방문해 주세요.
            for node in adjacentNodes:
                if node > 0 and node <= 10000 and visited[node] == 0:
                    visited[node] = 1
                    stack.append(node)
                    print('stack',stack)
    return False


def main():
    target = int(input())
    
    print(virusDFS(target))


if __name__ == "__main__":
    main()


#2번 바이러스#####
import queue;

def gossipCounts(n, graph):
    # 소문이 퍼진 횟수를 저장할 변수예요.
    count = 0
    
    #모든 노드를 순회할 필요가 없고, 시작 노드에서 모든 연결된 노드를 방문하고 다음 레벨의 노드로 이동하는 BFS 알고리즘이 더 효율적입니다.
    Q = queue.Queue();
    visited= []
    visited.append(1);

    Q.put(1)

    while not Q.empty():
        node = Q.get();
        count+=1
        for adjacentNodes in graph[node]:
            if adjacentNodes not in visited:
                visited.append(adjacentNodes)
                Q.put(adjacentNodes)
    
    return count -1


# 입력받은 pairs를 그래프 자료구조로 사용할 수 있도록 바꿔주는 함수에요.
def getGraph(n, pairs):
    graph = [[] for i in range(n+1)]
    m_edges = len(pairs)
    for pair in pairs :
        graph[pair[0]].append(pair[1])
        graph[pair[1]].append(pair[0])
    #print(pairs,'pairs',graph)
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


#3번 소풍#####
def getAdjacentNodes(studentsMap, i, j):
    #visitedNode[0], visitedNode[1]
    adjacentNodes = []
    # studentMap에서 상하좌우의 인접 노드를 구해 주세요.
    if i>0 and studentsMap[i-1][j] != 0:
        adjacentNodes.append((i-1,j))

    if i<len(studentsMap)-1 and studentsMap[i+1][j] != 0:
        adjacentNodes.append((i+1,j))

    if j>0 and studentsMap[i][j-1] != 0:
        adjacentNodes.append((i,j-1))
    
    if j<len(studentsMap[i])-1 and studentsMap[i][j+1] != 0:
        adjacentNodes.append((i,j+1))
    
    return adjacentNodes

def picnicCounts(n, studentsMap):
    classCounts = 0  # 반 전체 개수
    studentCountsForEachClass = {} # 각 반에 속한 학생 개수
    
    # 모든 노드에 대한 방문 정보를 담은 리스트를 정의해요.
    visited = [[False for i in range(n)] for j in range(n)] 
    
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and studentsMap[i][j] != 0:
                #print('i',i,'j',j)
                classCounts += 1
                studentCountsForEachClass[classCounts] = 0
                
                # 스택 구조를 정의해요.
                stack = []
                
                # (i, j) 좌표에 대한 방문이 완료되었으니 방문 정보를 갱신해 주세요.
                visited[i][j] = True
                
                # 방문이 완료되었으니, 노드를 스택에 추가해 주세요.
                stack.append((i,j))
                
                # 각 반에 속한 학생의 수를 갱신해 주세요.
                studentCountsForEachClass[classCounts] += studentsMap[i][j]
                #print('a')
                # 스택이 비어있지 않은 경우에만 반복문을 돌도록 조건을 설정해 주세요.
                while stack:
                    # 방문한 노드를 꺼내 주세요.
                    visitedNode = stack.pop()
                    
                    # 인접 노드를 계산해요.
                    adjacentNodes = getAdjacentNodes(studentsMap, visitedNode[0], visitedNode[1])
                   # print('b')
                    # 방문하지 않은 인접 노드를 방문해 주세요.
                    for node in adjacentNodes:
                        if not visited[node[0]][node[1]]:
                            visited[node[0]][node[1]] = True
                            stack.append(node)
                            studentCountsForEachClass[classCounts] += studentsMap[node[0]][node[1]]
                            #print(studentsMap[i][j])
                        #print('c',studentCountsForEachClass[classCounts])
                        
                    
    result = str(classCounts)
    sortedStudentCounts = sorted(studentCountsForEachClass.values())
    for i in range(classCounts):
        result += "\n"
        result += str(sortedStudentCounts[i])
    return result


def main():
    n= int(input())

    lines = [] 
    
    for _ in range(n):
        line = list(input())
        line = [int(x) for x in line]
        lines.append(line)
    
    #print('lines',lines)
    print(picnicCounts(n, lines))


if __name__ == "__main__":
    main()