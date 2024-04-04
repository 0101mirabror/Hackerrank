def capitalize_word (word : str     ) -> str:
    return  word[0].upper() + (word[1:] if len(word)>1  else '')
print(capitalize_word('s'))