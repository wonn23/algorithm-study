####그저 코드들을 이해한 것만으로도 만족할래여,, 다음엔 내가 풀 수 있겠지,, 나두 챗지피티의 뇌를 갖고싶다..#####

import sys
MAX_INT = sys.maxsize

def getShortest(graph, start, end):
    # 노드 개수 n, 확인 완료 노드 집합 S, 전체 노드 집합 V, 노드까지의 최소 거리를 저장할 Table을 초기화해요.
    # print(graph)
    n = len(graph)
    S = set([])
    V = set(range(0, len(graph)))
    Table = [MAX_INT for i in range(n)]
    # print(V - S)
    # 시작 노드에서 시작 노드까지의 거리 0을 Table에 설정해요.
    Table[start] = 0
    
    # 모든 노드를 확인할 때까지 반복해요.
    for i in range(n):
        minDistance = MAX_INT
        minNode = -1
        
        # 아직 확인이 안된 노드 집합(V-S) 중, 최소 거리 노드 minNode를 찾아 주세요.
        for node in (V - S):
            # print(Table[node],minDistance)
            if Table[node] < minDistance:
                minDistance = Table[node]
                # print(minDistance)
                minNode = node
                # print(minNode)
        # 최소 거리 노드 minNode를 확인 완료 노드 집합 S에 추가해요.
        S.add(minNode)
        # print("S",S)
        # 최소 거리 노드 minNode의 인접 노드에 대해 Table을 갱신해 주세요.
        for dest,cost in graph[minNode]:
            if Table[dest] > Table[minNode] + cost:
                Table[dest] = Table[minNode] + cost
            
    return Table[end]


def main():
    n, m, start, end = (int(x) for x in input().split())
    graph = [ [] for i in range(n) ]

    for i in range(m):
        line = [int(x) for x in input().split()]

        graph[line[0]].append((line[1], line[2]))
        graph[line[1]].append((line[0], line[2]))
    #line[1]번째 배열 자리에다가 값 넣어주라는 뜻
    print(getShortest(graph, start, end))


if __name__ == "__main__":
    main()








#####이거 하다가 리액트하면 아주 재밌음######

import sys
MAX_INT = sys.maxsize

def bellmanFord(graph, start, end):
    # 노드 개수 n, 확인 완료 노드 집합 S, 전체 노드 집합 V, 노드까지의 최소 거리를 저장할 Table을 초기화해요.
    n = len(graph)
    Table = [ MAX_INT for i in range(n) ]
    
    # 시작 노드의 거리 0을 Table[start]에 설정해요.
    Table[start] = 0
    
    # 최단 경로를 저장하는 Table을 갱신해 주세요.
    for i in range(n):
        for node in range(n):
            for destination, weight in graph[node]:
                if Table[node] != MAX_INT and Table[destination] > Table[node] + weight:
                    Table[destination] = Table[node] + weight
    
    # 조건을 수정하여 음수 사이클이 있는지 확인해요.
    for node in range(n):
        for destination, weight in graph[node]:
            # 음수 사이클의 존재 여부를 판단해 주세요.
            if Table[node] != MAX_INT and Table[destination] > Table[node] + weight:
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

