c = 0 #real answer
k = int(input())
for i in range(k):
    n = input()
    if n == 'X--':
        if i == k-1:
            print(c)
        c-=1
    elif n == '--X':
        c-=1
        if i == k-1:
            print(c)
    elif n == '++X':
        c+=1
        if i == k-1:
            print(c)
    elif n == 'X++':
        if i == k-1:
            print(c)
        c+=1

# fake answer

# c = 0
# # k = int(input())
# for i in range(k):
#     n = input()
#     if n == 'X--':
#         # print(c)
#         c-=1
#     elif n == '--X':
#         c-=1
#         # print(c)
#     elif n == '++X':
#         c+=1
#         # print(c)
#     elif n == 'X++':
#         # print(c)
#         c+=1
# print(c)