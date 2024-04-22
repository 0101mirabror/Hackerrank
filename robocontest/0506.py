n = int(input())
c = 0
k = 0
for i in range(1, n+1):
    c+=i 
    k+=c
print(k%(10**9+7))
 