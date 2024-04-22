x, y = map(float, input().split())
c = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    if b == 0:
        continue
    if x < a/b < y:
       c+=1
print(c)