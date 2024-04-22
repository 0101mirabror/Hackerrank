n = int(input())
c = 0
import re
for i in range(10**(n-1), 10**n):
    for k in range(n):
        if re.findall(list(str(i)), ['1', '3', '5', '7', '9']):
            c+=1
print(c)
