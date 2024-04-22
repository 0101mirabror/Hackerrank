n = input()
ls = []
while True:
    if 64 < int(n[:2]) < 100:
        ls += [int(n[:2])]
        n = n[2:]
    elif 99 < int(n[:3]) < 123:
        ls += [int(n[:3])]
        n = n[3:]
    if len(n) == 0:
        break
print(''.join([chr(i) for i in ls]))



