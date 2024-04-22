n, m = list(map(int, input().split()))
if  n == m != 0 :
    print(n*10 + 1, m*10 + 2)
elif n == 0 and m == 1:
    print(n , m)
elif m - n == 1:
    print(n*10+9, m*10)
else:
    print(-1)

