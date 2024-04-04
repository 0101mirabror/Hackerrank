import re
def func(s):
    return re.sub(r'\.', '-', s)
s = ''
print(func(s))