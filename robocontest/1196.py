a, b = list(map(int, input().split()[:2]))
 
print(a * (10**(len(str(b)))) + b)
