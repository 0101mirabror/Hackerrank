import re
n = input()

k = (re.match(r"^\+", n) or re.match(r"^\-", n)) and len(n.split('.'))==2 and (False if isinstance(int(n.split()[0]), int) or int(n.split()[0])=='.' else True)
print(n.split('.'))
print(True if k and float(n) else False)