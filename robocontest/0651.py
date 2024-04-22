a, b, c = list(map(int, input().split()))
p = (a+b+c)/2
from math import sqrt
s = sqrt(p*(p-a)*(p-b)*(p-c) )
k = max([a,b,c])
h = 2*s/k
print(round(h, 7))