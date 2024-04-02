def flick_switch(lst):
    k = []
    t = True
    for i in lst:
        if i == 'flick':
            t = False
            k.append(t)
        else:
            k.append(t)
    return k
# inp = ['codewars', 'flick', 'code', 'wars']
# inp = ['flick', 'chocolate', 'adventure', 'sunshine']
inp = ['bicycle', 'jarmony', 'flick', 'sheep', 'flick']
print(flick_switch(inp))