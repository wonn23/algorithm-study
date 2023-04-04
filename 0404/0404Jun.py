#그래프 알고리즘 기초 황준성

#---미션2 - 이상한 소문---


def gossipCounts(n, graph):
    # 소문이 퍼진 횟수를 저장할 변수예요.
    visited = [False] * (n + 1)
    count = 0
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            count += 1
    
    return count


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