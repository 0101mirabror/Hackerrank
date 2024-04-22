n = int(input())
lt = []
for i in range(n+1):
    if n == i + i%100:
        lt.append(i)
for j in sorted(lt):
    print(j, end=" ")
 