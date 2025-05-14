import sys
input = sys.stdin.readline 

N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0 

for i in range(N-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j +1]:
            cnt += 1
            arr[j], arr[j+1] = arr[j+1], arr[j]
            if cnt == K:
                print(*arr)
                sys.exit()

print(-1)
