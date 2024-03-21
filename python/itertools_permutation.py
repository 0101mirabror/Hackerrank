from itertools import permutations
command = input().split()
ls =  [i for i in command[0]]
# print(ls)
n = int(command[1])
k = sorted(list(permutations(ls, n)))
print(k)
for i in k:
    c = ""
    for j in i:
        c += j
    print(c)
# for i in 
