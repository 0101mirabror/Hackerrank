"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata `y` isn't considered a vowel.


"""

# VOWELS = ['a', 'e', 'i', 'o', 'u']
def disemvowel(text):
    text = text.replace('A', '')
    text = text.replace('E', '')
    text = text.replace('I', '')
    text = text.replace('O', '')
    text = text.replace('U', '')
    text = text.replace('a', '')
    text = text.replace('e', '')
    text = text.replace('i', '')
    text = text.replace('o', '')
    text = text.replace('u', '')
    return text

print(disemvowel('Mening ismim MirAbror'))

# best practice

def disemvowel2(text):
    for i in 'auioeAUIOE':
        text = text.replace(i, '')
    return text
print(disemvowel2("Abror"))