n, k = map(int, input().split()) 
ls = list(map(int, input().split()))
a = ls[k-1]
c = 0
if len(ls) > k: 
    for i in ls[k:]:
        if i == a:
            c+=1

print(c+k if sum(ls)>0 else 0)
