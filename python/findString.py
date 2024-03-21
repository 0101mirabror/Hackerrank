"""Find String"""

string1 = input()
string2 = input()
c = 0
print(string1.startswith(string2))
for i in range(len(string1)):
    if string1[i:len(string1)].startswith(string2):
        c+=1
print(c)
 
# string1.
# print(string1.find(string2))
# print(len(("".join(reversed(string1))).split(string2))-1 + len(string1.split(string2))-1)