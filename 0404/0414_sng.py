############################## 미션1

def virusDFS(target):
    # 스택 구조를 정의해요.
    stack = []
    
    # 탐색의 시작점 1을 정의해요.
    initialNode = 1
    
    # 0부터 10000까지의 노드에 대한 방문 정보를 담은 리스트를 정의해요.
    visited = [ 0 for i in range(0, 10001)]
    
    # 첫 번째 방문할 노드는 1이지요. 노드 1에 대한 방문 정보를 갱신해 주세요.
    visited[initialNode] = 1  
    
    # 방문이 완료되었으니, 노드 1을 스택에 추가해 주세요. append 메서드를 사용해 보세요.
    stack.append(initialNode)
    
    # 스택이 비어있지 않은 경우에만 반복문을 돌도록 조건을 설정해 주세요.
    while stack:
        # 방문한 노드를 꺼내 주세요.
        visitedNode = stack.pop()
        
        # 방문한 노드가 타겟 노드라면 탐색은 종료되고 True을 반환해요.
        if visitedNode == target:
            return True
            break
            
        else:
        # 인접 노드를 계산해요.
            adjacentNodes = filter(lambda x : x <= 10000, [visitedNode*2, visitedNode//3])
            # 방문하지 않은 인접 노드를 방문해 주세요.
            for adjacentNode in adjacentNodes:
                if visited[adjacentNode] == 0:   # 아직 방문하지 않은 노드가
                    visited[adjacentNode] = 1
                    stack.append(adjacentNode)
            
    return False


def main():
    target = int(input())
    
    print(virusDFS(target))


if __name__ == "__main__":
    main()




###################### 미션2
