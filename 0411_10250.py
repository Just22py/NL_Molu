t = int(input())

for i in range(t):
  h, w, n = map(int, input().split())
  floor = n % h
  no = n//h +1
  if (n % h == 0):
    floor = h
    no = n//h
  print(100*floor+no)
