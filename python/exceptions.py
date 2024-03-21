T = {}
for i in range(int(input())):
    ls1 = input().split()
    try: 
        print(int(ls1[0])/int(ls1[1]))
    except ZeroDivisionError as e:
        print("Error code: integer division or modulo by zero")
    except ValueError as e:
        print("Error code: ", e)
    # T[ls1[0]] = ls1[1]
# try:
#     for j in T:
#         print(type(j), j)
#         if int(T[j]) == 0:

#           print(int(j)/int(T[j]))
# except ZeroDivisionError or ValueError as e:
#     print("Error code:",e)
