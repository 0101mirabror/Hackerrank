l, b = map(int, input().split())
c = 0
while True: 
    c+=1
    l*=3
    b*=2
    if l > b:
        break
print(c)