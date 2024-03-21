import re
s = int(input())
# print(len(str))
for i in range(s):
    str = input()
    # match = re.search(r'[7-9]', str)
    # match = str.startswith(r'[7-9]')
    match = re.match(r'^(?:7|8|9)',str)
    print(match)
    # If-statement after search() tests if it succeeded
    if match and len(str) == 10 and str.isdigit():
        print('YES') ## 'found word:cat'
    else:
        print('NO')