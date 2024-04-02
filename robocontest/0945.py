a, b = list(map(int, input().split()))
print(a*b if a*b>2*(a+b) else 2*(a+b))