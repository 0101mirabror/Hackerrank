a, b = list(map(int, input().split()))
c = 0
if b > a:
    d = b - a
    while d >= 0:
        c += 1
        d -= 10
        if d in list(range(1,11)):
            print(c+1)
            break
elif a > b:
    k = a - b
    while k >= 0:
        c+=1
        k-=10
        if k in list(range(1, 10)):
            print(c+1)
            break
else:
    print(0)

