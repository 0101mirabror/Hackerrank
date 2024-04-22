s = 0
m = 0
a, n = map(int, input().split())
for i in range(1, n+1):
  s+=a**i
  m+=a**(-i)
print(s, m)
print(int(s//m))
