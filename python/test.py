nested_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    nested_list.append([name, score])
a = set([i[1] for i in nested_list])
second_grade = sorted(a)[1]

names = [i[0] for i in nested_list if second_grade == i[1]]
names.sort()

for name in names:
    print(name)
