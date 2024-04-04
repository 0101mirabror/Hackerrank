def func(coefficient, exponent):
    return f'{int(coefficient/(exponent+1))}x^{exponent+1}'
print(func(90, 2))
print(func(2, 1))