n = input()
def best_friend(n, a='h', b='e'):
    c = 0
    for i, j in enumerate(n):
        if j == a and  i+1 < len(n) and n[i+1] == b: 
            c+=1
            print(c, i,  j)
    return c
print(n.count('o') == best_friend(n=n, a='o', b='u'))

# best 
# def best_friend(t,a,b):
#  return t.count(a)==t.count(a+b)