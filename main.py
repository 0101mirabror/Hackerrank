students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

# Find the second lowest grade
grades = set([student[1] for student in students])
second_lowest = sorted(grades)[1]

# Find the students with the second lowest grade
names = [student[0] for student in students if student[1] == second_lowest]
names.sort()

# Print the names of the students with the second lowest grade
for name in names:
    print(name)