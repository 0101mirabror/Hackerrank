from math import gcd

print(gcd(5, 10))
a = list(map(int, input().split()))
b = max(a)
c = 6 - b + 1 
k = gcd(c, 6)
print(f'{int(c/k)}/{int(6/k)}')
