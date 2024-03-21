from collections import OrderedDict, Counter
ordered_dictionary = []
for i in range(int(input())):
    string = input().rsplit(" ", 1)
    ordered_dictionary.append((string[0], int(string[1])))
    # ordered_dictionary[string[0]] = string[1]
print(ordered_dictionary)
print(Counter(ordered_dictionary)) 

for j, i in Counter(ordered_dictionary).items():
    print(list(j)[0], list(j)[1]*i)
