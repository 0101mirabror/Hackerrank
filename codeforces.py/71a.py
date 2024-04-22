n = int(input())
for _ in range(n):
    m = input()
    k = f'{len(m) - 2}'
    print(m[0]+k+m[-1] if len(m) > 10 else m)