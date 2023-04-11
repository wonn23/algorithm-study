## 실습1 - 다익스트라
import sys
MAX_INT = sys.maxsize

def getShortest(graph, start, end):
    # 노드 개수 n, 확인 완료 노드 집합 S, 전체 노드 집합 V, 노드까지의 최소 거리를 저장할 Table을 초기화해요.
    n = len(graph)
    S = set([]) # 오... set은 집합 자료형으로 초기화해서 V-S 같은 집합을 구할 수 있다
    V = set(range(0, len(graph)))
    Table = [MAX_INT for i in range(n)]
    #print(graph)
    # 시작 노드에서 시작 노드까지의 거리 0을 Table에 설정해요.
    Table[start] = 0
    
    # 모든 노드를 확인할 때까지 반복해요.
    for i in range(n):
        minDistance = MAX_INT
        minNode = -1
        
        # 아직 확인이 안된 노드 집합(V-S) 중, 최소 거리 노드 minNode를 찾아 주세요.
        for node in (V - S):
            if Table[node] < minDistance:
                minDistance = Table[node]
                minNode = node

        # 최소 거리 노드 minNode를 확인 완료 노드 집합 S에 추가해요.
        S.add(minNode)
        
        # 최소 거리 노드 minNode의 인접 노드에 대해 Table을 갱신해 주세요.
        for pair in graph[minNode]:
            adjNode = pair[0]
            adjDist = pair[1]
            if Table[adjNode] > Table[minNode] + adjDist:
                Table[adjNode] = Table[minNode] + adjDist

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

## 실습 2 - 벨만 포드

import sys
MAX_INT = sys.maxsize

def bellmanFord(graph, start, end):
    # 노드 개수 n, 확인 완료 노드 집합 S, 전체 노드 집합 V, 노드까지의 최소 거리를 저장할 Table을 초기화해요.
    n = len(graph)
    Table = [ MAX_INT for i in range(n) ]
   # print(graph)
    
    # 시작 노드의 거리 0을 Table[start]에 설정해요.
    Table[start] = 0
    
    # 최단 경로를 저장하는 Table을 갱신해 주세요.
    for i in range(n-1): # 모든 노드를 최대 n-1 번만 탐색한다
        for j in range(n): # 모든 노드에 대해
            for destination, weight in graph[j]: # 해당 노드와 연결된 모든 에지를 탐색합니다.
                if Table[j] != MAX_INT and Table[destination] > Table[j] + weight:
            # 만약 (출발 노드에서 해당 에지로 이동하는 비용) + (해당 에지의 도착 노드까지의 현재 최단 거리) 가
            # (해당 도착 노드까지의 현재 최단 거리) 보다 작다면
                    Table[destination] = Table[j] + weight # 해당 도착 노드의 최단 거리를 업데이트합니다.
    
    # 조건을 수정하여 음수 사이클이 있는지 확인해요.
    for node in range(n):
        for destination, weight in graph[node]:
            # 음수 사이클의 존재 여부를 판단해 주세요.
            if Table[j] != MAX_INT and Table[destination] > Table[node] + weight:
                return "음수 사이클이 존재해요."
    
    return Table[end]


def main():
    n, m, start, end = (int(x) for x in input().split())
    graph = [ [] for i in range(n) ]

    for i in range(m):
        line = [int(x) for x in input().split()]
        graph[line[0]].append((line[1], line[2]))

    print(bellmanFord(graph, start, end))


if __name__ == "__main__":
    main()
