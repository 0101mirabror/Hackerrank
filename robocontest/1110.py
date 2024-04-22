for i in range(int(input())):
    e, o = 0, 0
    n = int(input())
    for j in range(1, n+1):
        if j%2 == 0 and n%j == 0:
            e += 1
        elif j%2 == 1 and n%j == 0:
            o += 1
    print(e, o)
    if e == o:
        print('YES')
    else:
        print('NO')
