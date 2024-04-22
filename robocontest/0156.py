n, m = list(map(int, input().split()))
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
c = 0
for i in l2:
    k = 0
    for j in l1:
        # print(i, j, i%j)
        if i%j == 0:
            k+=1
    if len(l1) == k:
        c += 1
print(c)