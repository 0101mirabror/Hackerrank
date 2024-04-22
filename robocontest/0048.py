n = int(input())
# numbers (n**2-n)/2+n
lt = [i for i in range(1, ((n**2 - n) // 2 + n) + 1)]

for i in range(1, n+1):
    print(f'{lt[:i]}'.replace('[', '').replace(']', '').replace(',', ''))
    lt = lt[i:]