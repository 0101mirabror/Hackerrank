for i in range(int(input())):
    k, q, n = list(map(int, input().split()))
    c = 0
    d = (q+k)*2
    for j in range(n-1):
        d = (d+k)*2 
    print(d)