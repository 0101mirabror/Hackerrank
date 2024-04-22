a, b, c, d = list(map(int, input().split()))
n = 0
m = 0
while c < 10000:
  a +=b
  c +=d
  print(n, a, c)
  if a == c:
    m = 1
  n+=1
if m > 0:
  print("YES")
else:
  print("NO")