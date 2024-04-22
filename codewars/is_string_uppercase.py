# def is_uppercase(inp:str):
#     return False if inp.islower() else True

# print(is_uppercase('hello I AM DONALD'))
# inp = 'hello I AM DONALD'
inp = '2 I AM DONALD'

def is_uppercase(inp: str):
    return  all([(i.isupper() or not i.isalpha()) for i in inp])
print(is_uppercase(inp))