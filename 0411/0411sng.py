################# 실습1
import sys
MAX_INT = sys.maxsize

def getShortest(graph, start, end):
    # 노드 개수 n, 확인 완료 노드 집합 S, 전체 노드 집합 V, 노드까지의 최소 거리를 저장할 Table을 초기화해요.
    n = len(graph)
    S = set([])
    V = set(range(0, len(graph)))
    Table = [MAX_INT for i in range(n)]  # 거리(가중치)가 아직 나오지 않았기 때문
    
    # 시작 노드에서 시작 노드까지의 거리 0을 Table에 설정해요.
    Table[start] = 0
    

    # 모든 노드를 확인할 때까지 반복해요.
    for _ in range(n):    # i는 "노드 번호"를 뜻함
        minDistance = MAX_INT   # 초기 minDistance는 모두 무한대값, 거리(가중치)가 아직 나오지 않았기 때문
        minNode = -1   # 0~7를 제외한 나머지 수들로 대체 가능(None도 가능)
        
        # 아직 확인이 안된 노드 집합(V-S) 중, 최소 거리 노드 minNode를 찾아 주세요.
        for node in (V - S):   # 초기 (V-S) = {0,1,2,3,4,5,6,7}
            if Table[node] < minDistance:
                minDistance = Table[node]
                minNode = node

        # 최소 거리 노드 minNode를 확인 완료 노드 집합 S에 추가해요.
        S.add(minNode)
        
        # 최소 거리 노드 minNode의 인접 노드에 대해 Table을 갱신해 주세요.

        for pair in graph[minNode]:
            adjNode, adjDis = pair   # cur_dis = 인접노드와 minNode와의 거리
            dis = adjDis + Table[minNode]  # Table[minNode] = 시작노드부터 minNode까지의 최소거리
            if Table[adjNode] > dis:
                Table[adjNode] = dis
            else:
                Table[adjNode] = Table[adjNode]
                    
    
    return Table[end]


def main():
    n, m, start, end = (int(x) for x in input().split())
    graph = [ [] for i in range(n) ]

    for i in range(m):
        line = [int(x) for x in input().split()]

        graph[line[0]].append((line[1], line[2]))
        graph[line[1]].append((line[0], line[2]))

    print(getShortest(graph, start, end))


if __name__ == "__main__":
    main()
    
    
    
################# 실습2는 다 풀면 올리겠습니다 ㅠㅅㅠ
