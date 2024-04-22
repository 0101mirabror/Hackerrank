n = list(map(int, input().split()[:2]))
# print(n)
if len(n) == 1:
    m = int(input())
    print(m * n[0])
else:
    print(sum(n))

