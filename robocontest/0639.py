n = int(input())
c = 0
b = 1
while True:
    
    c+=b*(b+1)/2
    if c > n:
        print(b-1)
        break
    b+=1
   
