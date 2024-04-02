import re
# m = re.search(r'\d+','1234')
m = re.search(r'aa','aaadaa')
print(m.end())
print(m.start())
k = [ (m.start(), m.end()) for i in range(len('aaadaa'))]