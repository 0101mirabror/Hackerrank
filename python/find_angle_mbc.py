import math
a = int(input())
b = int(input())  
s = a*b/2
g = math.sqrt(b*b+a*a)
# print(f"sinx:{(2*s)/(a*b)}", math.degrees(math.asin(a/(math.sqrt(a*a+b*b)))))
BAC = math.degrees(math.asin(a/(math.sqrt(a*a+b*b))))
m = (1/2)*math.sqrt(b*b+ a*a) # mediana in hypotenuse
print(BAC, g)
print(m)
print(str(math.ceil(math.degrees(math.asin(a/(2*m)))))+"\u00B0")

 