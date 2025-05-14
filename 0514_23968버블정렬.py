import sys
input = sys.stdin.readline 

N, K = map(int, input().split())
arr = list(map(int, input().split()))
result = -1
cnt = 0 

for i in range(N-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j +1]:
            cnt += 1
            arr[j], arr[j+1] = arr[j+1], arr[j]
            if cnt == K:
                result = arr[j], arr[j+1]
                break

if result == -1:
    print(result)

else: 
     for i in result:
        print(i, end=" ")
