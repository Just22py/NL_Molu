from collections import deque

N,M,V = map(int, input().split())

graph = [[0]*(N + 1) for i in range (N + 1)]
for j in range(M):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


visited = [0]*(N+1)
def dfs(V):
    visited[V] = 1
    print(V, end = ' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited[i] ==0:
            dfs(i)
            
visited2 = [0] * (N + 1)

def bfs(V):
    q = deque()
    q.append(V)
    visited2[V] = 1
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in range(1, N + 1):
            if graph[x][i] == 1 and not visited2[i]:  # Check adjacency and visit status
                q.append(i)
                visited2[i] = 1


dfs(V)
print() 
bfs(V)
