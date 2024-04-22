n = input()
ls = list(map(int, n.split('+')))
ls.sort()
print('+'.join([str(i) for i in ls]))