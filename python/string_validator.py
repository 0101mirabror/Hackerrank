s = input()
"1"
c = {1: False, 2: False, 3: False, 4: False, 5: False}
for i in s:
        if i.isdigit() and c[3] == False:
            c[3] = True   
        if i.islower() and c[4] == False:
            c[4] = True
        if i.isupper() and c[5] == False:
            c[5] = True
        if i.isalnum() and c[1] == False: 
            c[1] = True
        if i.isalpha() and c[2] == False:
            c[2] = True
        
print(c)
for i in c.values():
        print(i)
# "2"
# for i in s:
#     if i.isalpha():
#         print(True)
#         break
# for i in s:
#     if i.isdigit():
#         print(True)
#         break
# for i in s:
#     if i.isupper():
#         print(True)
#         break
# for i in s:
#     if i.islower():
#         print(True)
#         break
# for i in s:
#     if i.isalnum():
#         print(True)
#         break