X = 0
n = int(input())
for _ in range(n):
    oper = input()
    if oper == 'X++':
        if _ == n-1:
            print(X)
        X+=1
    elif oper == '++X':
        X+=1
        if _ == n-1:
            print(X)
    elif oper == 'X--':
        if _ == n-1:
            print(X)
        X-=1
    elif oper == '--X':
        X-=1
        if _ == n-1:
            print(X)
# print(X)

