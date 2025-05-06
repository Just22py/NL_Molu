import sys
sys.setrecursionlimit(10000)

t = int(input())
def dfs (x, y):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    for i in range(4):
        searchx = x + dx[i]
        searchy = y + dy[i]
        if (0 <= searchx <m) and (0 <= searchy < n) and bachufield[searchy][searchx] == 1:
            bachufield[searchy][searchx] = 0
            dfs(searchx,searchy)


for _ in range(t):
    m, n, k = map(int, input().split())
    bachufield = [[0]*(m+1) for _ in range (n)]

    for _ in range (k):
        X, Y = map(int, input().split())
        bachufield[Y][X] = 1


    count = 0 
    for i in range(m):
        for j in range(n):
            if bachufield[j][i] == 1:
                dfs(i,j)
                count += 1
    print(count)


  
