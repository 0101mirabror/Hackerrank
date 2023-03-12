nested_list = []
print(44)
# for i in range(int(input())):
#     name = input()
#     score = float(input())
#     nested_list.append([name, score])
nested_list = [['al', 45], ['mon', 55], ["tue", 23], ["tue", 23],['fri', 45]]
a = set([i[1] for i in nested_list])
second_lowest = (sorted(a))[1]
names = [student[0] for student in nested_list if student[1]==second_lowest] 
names.sort()
for name in names:
    print(name)

print(dir(set))
k = set([12,12,56,56,35,335,24,56,23,12,85,85])
# print(sorted(k),nested_list, second_lowest)
