from itertools import combinations_with_replacement
string = input().split()
word = string[0]
num = int(string[1])
k = list(combinations_with_replacement(sorted(word), num))
# print(list(combinations_with_replacement(sorted(word), num)))
for i in k:
    c = ""
    for j in range(len(i)):
        c += i[j]
    print(c)
