n = input()
print(sum(list(map(int, n))) if int(n) > 0 else sum(list(map(int, n[1:]))))