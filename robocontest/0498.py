m = 0
t = 0
for _ in range(int(input())-1):
    a, b = list(map(int, input().split()[:2]))
    m += a  
    t += b
men = int(input())
print(0 if men >= m else men - t)