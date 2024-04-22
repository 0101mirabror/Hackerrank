n = int(input())
for _ in range(n):
    a, b, c, d = list(map(int, input().split()))
    print(c+(c-a), d+(d-b))