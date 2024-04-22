l: int = int(input())
lt = []
for _ in range(l):
    a: str = input()
    lt.append(a)
print(lt)
import re
for i in lt:
    is_alpha = bool(re.match(r'^[a-zA-Z0-9]+$', i))
    is_uniq = bool(re.match(r'^(?!.*(.).*\1)[\S\s]+$', i))
    is_3 = bool(re. match(r'\d.*\d.*\d', i))
    is_2U = bool(len(re.findall(r'[A-Z]', i)) >= 2)
    is_len = bool(len(i) == 10)
    print(is_alpha, is_uniq, is_3, is_2U, is_len)
    