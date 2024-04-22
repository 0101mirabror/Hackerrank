n = int(input())
 
if n % 5 == 0:
    print(n//5)
elif (n%5)%3 == 0:
    print(n//5 + 1)
elif n%3 == 0:
    print(n//3)
else:
    print(-1)