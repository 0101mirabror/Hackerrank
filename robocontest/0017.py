k = []
n = int(input())
c=1
for i in range(1, 250):
    print(c, pow(sum([int(i) for i in str(c)]),2))
    if c%pow(sum([int(i) for i in str(c)]),2)==0:
        k.append(c)
    c+=1

print( k)