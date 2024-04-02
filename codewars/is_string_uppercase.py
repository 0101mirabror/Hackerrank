def is_uppercase(inp:str):
    return False if inp.islower else True

print(is_uppercase('hello I AM DONALD'))
inp = 'hello I AM DONALD'
print(not inp.isalpha())