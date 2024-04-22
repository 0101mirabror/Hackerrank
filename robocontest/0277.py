for _ in range(int(input())):
    N, K = list(map(int, input().split()))
    lt = list(map(int, input().split()[:N]))
    lr = [i for i in lt if i <= 0]
    if K <= len(lr):
        print('Qizg\'in')
    else:
        print('Zerikarli')