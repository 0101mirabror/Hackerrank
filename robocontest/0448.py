a, b, c, x = list(map(int, input().split()))
print('YES' if a*(x**2) + b*x + c == 0 else 'NO')