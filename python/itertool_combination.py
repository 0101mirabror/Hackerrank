from itertools import combinations
string = input().split()
word = string[0]
num = int(string[1])
k = []
for i in range(1, num+1):
    k.append(sorted(list(combinations(sorted(word), i))))
print(k)
for j in k:
    # print("j", j)
    # c = ""
    for l in j:
        # print("l", l)
        c = ""
        for m in range(len(l)):
            c+=l[m]
        print(c)
        #     print(m)