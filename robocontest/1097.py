n = input()
for i in enumerate(n):
    if int(i[1]) < 9:
        n = n.replace(i[1], '9', 1)
        break
print(n)