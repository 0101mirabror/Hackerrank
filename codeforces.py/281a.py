n = input()
print(n[0].upper() + n[1:] if len(n) > 1 else n[0].upper())