import math
x, y = list(map(float, input().split()))
m1 = 1/(x + 2/(x**2) + 3/(x**3))
m2 = math.e ** (x**2 + 3*x)
m3 = math.atan(x+y) + abs(5+x)**2
m4 = math.cos(y**2 + (x**2)/2)**2
print(round((m1 + m2) / m3 - m4, 2))
