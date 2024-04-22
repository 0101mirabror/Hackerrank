c = 0
for i in range(int(input())):
    ls = list(map(int, input().split()))
    if sum(ls) >= 2:
        c+=1
print(c)