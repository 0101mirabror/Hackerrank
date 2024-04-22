a, b = list(map(int, input().split()[:2])) 
# print(sum([a for a in range(a, b+1) if a % 3 == 0 and a % 7 != 0]))
print(sum(filter(lambda x: x%3==0 and x%7!=0, range(a, b+1))))