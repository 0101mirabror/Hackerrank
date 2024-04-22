l = []
import math
for _ in range(3):
    m = list(map(int, input().split()))
    l += m
    
print(l)
a, b, c, d, e, f = l
x = math.sqrt((c-a)**2 + (d-b)**2)
y = math.sqrt((e-a)**2 + (f-b)**2)
z = math.sqrt((c-e)**2 + (d-f)**2)
print('uchburchak' if x+y>z and x+z>y and y+z>x else 'uchburchak emas')