n= int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range (n+1) ]
visited = [0] * (n+1)
result = []

for _ in range(m):
    x , y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

    
def dfs(v,chon):
    chon += 1
    visited[v] = 1

    if v == b:
        result.append(chon)
    
    for i in graph[v]:
        if visited[i]== 0:
            dfs(i,chon)
        
dfs(a,0)
if result:
    print(result[0]-1)
else:
    print(-1)
