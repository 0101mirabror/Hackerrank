def multiply_number(n):
    return n * pow(5, (len(str(n)) if n >=0 else len(str(n))-1))
print(multiply_number(3))
print(multiply_number(200))
print(multiply_number(10))
print(multiply_number(-3))
print(multiply_number(0))