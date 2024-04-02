n = int(input())
ls = list(map(int, input().split()[:n]))
print(sorted(ls,reverse=True)) 
print(print(ls[0]) if len(ls) == ls.count(max(ls)) else sorted(ls, reverse=True)[ls.count(max(ls))])