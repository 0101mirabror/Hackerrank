string = input()
l = []
c = 0
for i in range(len(string)):
    if string[i].isupper():
        m = string[i:].index(string[i])
        l.append(c+m)
    c+=1
print(l)