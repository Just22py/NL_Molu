a, b = map(int, input().split())
def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

l = a*b//gcd(a,b)

print(gcd(a,b))
print(int(l))
