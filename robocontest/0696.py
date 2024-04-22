n = int(input())
c = 0
a = 2
primes = []
while c <= n:
    b = 0
    for i in range(2, a+1):
        if a%i == 0:
            b+=1
    if b == 1:
        primes.append(i)
        c+=1
    a+=1
seq = [2]
k = 2
for j in primes[1:]:
    k += j
    seq.append(k)

print(sum(seq[:-1]))



# a = 0
# b = 2
# c = 0
# n = 5
# while c<=5:
#     print((c, b))
    
#     for i in range(2, b+1):
#         print(i)
#         if b%i == 0:
#             a+=1
#     if a < 2:
#         c+=1
#     if b == 3:
#         break 
#     b += 1
    
    

