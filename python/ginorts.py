string = input()
# print(sorted(string))
k = [i for i in sorted(string) if (lambda x: x.islower())(i)]
u = [i for i in sorted(string) if (lambda x: x.isupper())(i)]
num = [i for i in sorted(string) if (lambda x: x.isdigit())(i)]
odd= [i for i in num if (lambda x: x%2==1)(int(i))]
even = [i for i in num if (lambda x: x%2==0)(int(i))]
c = ""
for i in k+u+odd+even:
    c+=i
print(c)
