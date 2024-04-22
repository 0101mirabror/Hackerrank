a, c, k = list(map(int, input().split()))

counter = 0
for i in range(1, a+1):
    if  i % c == k:
        counter+=1
         
# print(counter)

# print(sum([1 for i in range(1, a+1) if i%c == k]))
print(len(range(k, a+1, c)) if c != k else 0 )
