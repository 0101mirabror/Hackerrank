a, b, c = list(map(int, input().split()))
d, e, f = list(map(int, input().split()))
print(3600*(d-a)+60*(e-b)+(f-c))