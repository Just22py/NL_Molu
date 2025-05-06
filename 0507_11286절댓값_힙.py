import heapq
import sys
input =  sys.stdin.readline

n=int(input())
base = []

for _ in range(n):
    x=int(input())
    if x != 0:
        heapq.heappush(base, (abs(x),x))
    else:
        if base:
            print(heapq.heappop(base)[1])
        else:
            print(0)
