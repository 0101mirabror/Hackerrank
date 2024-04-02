def how_much_i_love_you(nb_petals):
    petal_words = {
        1: 'I love you', 2: 'a little', 3:'a lot', 4: 'passionately', 5: 'madly', 6: 'not at all'
    }
    return petal_words[nb_petals] if nb_petals <= 6 else petal_words[6] if nb_petals%6==0 else petal_words[nb_petals%6]
print(how_much_i_love_you(132))

'''best'''
# def how_much_i_love_you(nb_petals):
#     return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1] #g