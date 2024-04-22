n, m, k, d = map(int, input().split())
print(n*m+d if n*m+d<k*n else k*n)