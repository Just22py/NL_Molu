n = int(input())
arr = list(map(int, input().split()))

m = [0] * n
m[0] = arr[0]

for i in range(1, n):
    if arr[i] > m[i-1] + arr[i]:
        m[i] = arr[i]
    else:
        m[i] = m[i-1] + arr[i]

print(max(m))
