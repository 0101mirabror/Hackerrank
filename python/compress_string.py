from itertools import groupby

def split_consecutive_characters(string):
    result = []
    accumulation = ""
    for char in string:
        if char == accumulation[-1:]:
            accumulation += char
        else:
            if accumulation:
                result.append(accumulation)
            accumulation = char
    if accumulation:
        result.append(accumulation)
    return result

# dt = {}
# dt = [(len(i), i[0]) for i in split_consecutive_characters(input())]

for i in split_consecutive_characters(input()):
    print((len(i), int(i[0])), end=" ")
        
