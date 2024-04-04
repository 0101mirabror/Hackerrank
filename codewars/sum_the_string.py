def func(a,b):
    a = 0 if a == '' else a
    b = 0 if b == '' else b
    return eval(f"{a}+{b}")
print(func("4", "5"))