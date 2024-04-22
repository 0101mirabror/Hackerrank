n = int(input())
c = 0
# for i in range(n+1):
#     c += (1+3*i+3*i**2)
# print(c)
print(sum([1+3*i+3*i**2 for i in range(n+1)]))