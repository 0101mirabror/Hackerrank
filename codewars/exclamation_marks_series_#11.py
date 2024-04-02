def replace_exclamation(st):
    for i in st:
        if i in 'aeiouAEIOU':
            st = st.replace(i, '!')
    return st


st = input()
print(replace_exclamation(st))