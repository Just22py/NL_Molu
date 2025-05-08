A, P = map(int, input().split())

seq = [A]

while True:
    res = 0
    for i in str((seq[-1])):
        res += int(i) ** P
       
    if res in seq:
       fin = seq.index(res)
       break

    seq.append(res)
   

print(fin)
