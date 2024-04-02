import re
b, a = list(map(int, input().split()))
def fact(n, m=1):
    if n == m:
        return m
    return n*fact(n-1)
# m = fact(48, 5)
m = fact(a, b)
print(re.search(r'[1-9]', str(m)[::-1]).span()[0])