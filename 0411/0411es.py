#0411 그래프 알고리즘 심화(다익스트라, 벨만-포드)


#최단 거리 구하기###

import sys
MAX_INT = sys.maxsize

def getShortest(graph, start, end):
    # 노드 개수 n, 확인 완료 노드 집합 S, 전체 노드 집합 V, 노드까지의 최소 거리를 저장할 Table을 초기화해요.
    n = len(graph)
    S = set([])
    V = set(range(0, len(graph)))
    Table = [MAX_INT for i in range(n)]
    #print(n)
    # 시작 노드에서 시작 노드까지의 거리 0을 Table에 설정해요.
    Table[start] = 0
    
    #print(graph)
    # 모든 노드를 확인할 때까지 반복해요.
    for i in range(n):
        minDistance = MAX_INT
        minNode = -1
        # 아직 확인이 안된 노드 집합(V-S) 중, 최소 거리 노드 minNode를 찾아 주세요.
        for node in (V - S):
            if Table[node] < minDistance :
                minDistance = Table[node];
                minNode = node;

        # 최소 거리 노드 minNode를 확인 완료 노드 집합 S에 추가해요.
        S.add(minNode)
        
        # 최소 거리 노드 minNode의 인접 노드에 대해 Table을 갱신해 주세요.
        for pair in graph[minNode]:
            Adja, dist = pair #pair 프린트해보면 (1,3) (5,1) ... 으로 인접 노드랑 거리가 나옴. 그걸 Adja dist에 각각 할당
            Table[Adja] = min(Table[Adja], Table[minNode]+dist)
    
    return Table[end]



# 벨만-포드 : 힘을 아낄 수 있는 하루 ###
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


import sys
MAX_INT = sys.maxsize

def bellmanFord(graph, start, end):
    # 노드 개수 n, 확인 완료 노드 집합 S, 전체 노드 집합 V, 노드까지의 최소 거리를 저장할 Table을 초기화해요.
    n = len(graph)
    Table = [ MAX_INT for i in range(n) ]
    S = set([])
    V = set(range(0,n))
    
    # 시작 노드의 거리 0을 Table[start]에 설정해요.
    Table[start] = 0
    
    # 최단 경로를 저장하는 Table을 갱신해 주세요.
    # n-1만큼 반복
    for _ in range(1, n):
        for node in range(n):
            for pair in graph[node]:
                Adja, dist = pair
                if Table[node] != MAX_INT and Table[node]+dist < Table[Adja]:
                    Table[Adja] = Table[node] + dist
        
    # 조건을 수정하여 음수 사이클이 있는지 확인해요.
    # n번째에서는 테이블이 갱신이 되면 안됨!!! 여기서 갱신되는 순간  . .. 마이너스마이너스마이너스.... .
    # 앞에서 n-1번 순회하면서 최단 경로를 구했기 때문에, 마지막에 음수 사이클이 있는지 확인하기 위해서 n번 돌리면서 한번 좌라락 보는 거임.

    for node in range(n):
        for destination, weight in graph[node]:
            # 음수 사이클의 존재 여부를 판단해 주세요.
            if Table[node] != MAX_INT and Table[node] + weight < Table[destination]:
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
