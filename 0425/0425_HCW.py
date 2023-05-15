## 9251 LCS 

s1 = input()
s2 = input()
n = len(s1)
m = len(s2)

Table = [[0 for _ in range(m)] for _ in range(n)]

if s1[0] == s2[0]:
    Table[0][0] = 1

for i in range(1, n):
    if s1[i] == s2[0]:
        Table[i][0] = 1
    else:
        Table[i][0] = Table[i-1][0]

for i in range(1, m):
    if s2[i] == s1[0]:
        Table[0][i] = 1
    else:
        Table[0][i] = Table[0][i-1]

for i in range(1, n):
    for j in range(1, m):
        if s1[i] == s2[j]:
            Table[i][j] = Table[i-1][j-1] + 1
        else:
            Table[i][j] = max(Table[i-1][j], Table[i][j-1])
            
print(Table[-1][-1])


# 17204 죽음의 게임

n, k = map(int,input().split())
graph = []
visited = [False for i in range(n)]
for i in range(n):
    graph.append([i,int(input())])
visited[0] = True
stack = []
count = 1
stack.append(graph[0][1])
while stack:
    v = stack.pop()
    if k == v:
        print(count)
        break
    elif visited[v] == False:
        visited[v] =True
        count += 1
        stack.append(graph[v][1])
    else:
        print(-1)
