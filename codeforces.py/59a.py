n = input()
k = len([i for i in n if i.isupper()]) > len([i for i in n if i.islower()])
print(n.upper() if k else n.lower()) 