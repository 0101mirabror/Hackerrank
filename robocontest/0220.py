l = int(input())
r = int(input())
n = int(input())
print(1 if sum(list(map(int, list(str(l)))))== n else 'lll')
while True:
    print(l)
    if sum(list(map(int, list(str(l))))) == n:
        print(l)
        break
    else:
        l+=1
    
    if l+15>0:
        break