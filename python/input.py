string  = input().split()
x = int(string[0])
y = int(string[1])
oper = input().replace("x", f"{x}")
# print(oper)
if eval(oper) == y:
    print(True)
else:
    print(False)