from collections import namedtuple

num = int(input())
columns = input()
Student = namedtuple("Student", columns)
s = 0
for i in range(num):
    data = input().split()
    student = Student(data[0], data[1], data[2], data[3])
    s += int(student.MARKS)
print(round(s/num, 2))