def dfs(start, depth):
    if depth == 6:
        print(*ans)
        return
    for i in range(start,n):
        ans.append(num[i])
        dfs(i+1, depth+1)
        ans.pop()

while 1:
    t = list(map(int, input().split()))
    n, num = t[0], t[1:]
    if n==0:
        break
    ans = []
    dfs(0,0)
    print()