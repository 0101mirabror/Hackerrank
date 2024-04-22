n = int(input())
ls = list(map(int, input().split()[:n]))
dt = {
    1 : ls.count(1), 2 : ls.count(2), 3 : ls.count(3), 
    4 : ls.count(4), 5 : ls.count(5)     
}
k = 1
m = ls.count(1)
for i, j in dt.items():
    if m < j:
        k = i
        m = j
print(k) 
 
# k = list(dt.keys()).count(max(list(dt.keys())))
# print(dt[max(dt.keys())] if k == 1 else dt[min(dt.keys())])