n, a, b = list(map(int, input().split()[:3]))
print('{0:.5f}'.format((100 - a) * n / (100 - b)))