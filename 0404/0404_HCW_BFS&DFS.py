### 미션1 - 바이러스 ###

def virusDFS(target):
    # 스택 구조를 정의해요.
    stack = []
    
    # 탐색의 시작점 1을 정의해요.
    initialNode = 1
    
    # 0부터 10000까지의 노드에 대한 방문 정보를 담은 리스트를 정의해요.
    visited = [ 0 for i in range(0, 10001)]
    
    # 첫 번째 방문할 노드는 1이지요. 노드 1에 대한 방문 정보를 갱신해 주세요.
    # visited[1] = 1
    
    # 방문이 완료되었으니, 노드 1을 스택에 추가해 주세요. append 메서드를 사용해 보세요.
    stack.append(initialNode)
    
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
            if adjacentNodes[0]> 10000:
                adjacentNodes[0] = visitedNode
            # 방문하지 않은 인접 노드를 방문해 주세요.
            if visitedNode not in visited:
                visited[visitedNode] = visitedNode
                stack.extend(adjacentNodes)
            
    return False


def main():
    target = int(input())
    
    print(virusDFS(target))


if __name__ == "__main__":
    main()


### 미션 2 - 이상한 소문 ###

from collections import deque

def gossipCounts(n, edges):
    graph = [[] for _ in range(n+1)]
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    
    visited = [False] * (n+1)
    visited[1] = True
    q = deque([1])
    count = 0
    
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                count += 1
                
    return count

n_nodes = int(input())
n_edges = int(input())

edges = [list(map(int, input().split())) for _ in range(n_edges)]

print(gossipCounts(n_nodes, edges))


### 미션 3 - 유치원 소풍 ###

def getAdjacentNodes(studentsMap, x, y):
    adjacentNodes = []
    # studentMap에서 상하좌우의 인접 노드를 구해 주세요.
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx , ny = x + dx , y+ dy
        if 0 <= nx and nx < len(studentsMap) and  0 <= ny and ny < len(studentsMap):
            adjacentNodes.append([nx,ny])
        
    return adjacentNodes

def picnicCounts(n, studentsMap):
    classCounts = 0  # 반 전체 개수
    studentCountsForEachClass = {} # 각 반에 속한 학생 개수
    
    # 모든 노드에 대한 방문 정보를 담은 리스트를 정의해요.
    visited = [[False for i in range(n)] for j in range(n)] 
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and studentsMap[i][j] != 0:
                classCounts += 1
                
                cnt = 1
                # 스택 구조를 정의해요.
                stack = []
                
                # (i, j) 좌표에 대한 방문이 완료되었으니 방문 정보를 갱신해 주세요.
                visited[i][j] = True
                
                # 방문이 완료되었으니, 노드를 스택에 추가해 주세요.
                stack.append([i,j])
                
                # 스택이 비어있지 않은 경우에만 반복문을 돌도록 조건을 설정해 주세요.
                while stack:
                    # 방문한 노드를 꺼내 주세요.
                    visitedNode = stack.pop()
                    # 인접 노드를 계산해요.
                    adjacentNodes = getAdjacentNodes(studentsMap, visitedNode[0], visitedNode[1])
                    
                    # 방문하지 않은 인접 노드를 방문해 주세요.
                    for nx,ny in adjacentNodes:
                        if not visited[nx][ny] and studentsMap[nx][ny] == 1:
                            visited[nx][ny] = True
                            stack.append([nx,ny])
                            cnt += 1
                studentCountsForEachClass[classCounts]=cnt
                    
    result = str(classCounts)
    sortedStudentCounts = sorted(list(studentCountsForEachClass.values()))
    for i in range(classCounts):
        result += "\n"
        result += str(sortedStudentCounts[i])
    return result


def main():
    n = int(input())


    lines = [list(map(int, input().strip())) for _ in range(n)]
    
    print(picnicCounts(n, lines))

if __name__ == "__main__":
    main()
