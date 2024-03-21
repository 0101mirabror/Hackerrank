"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def vowel_count(string):
    c = 0
    for i in "aeiou":
        print(i)
        for n in string:
            print(n)
            if i == n:
                c+=1
    return c
print(vowel_count("dadauiii"))


def vowel_count(string):
    c = 0
    for i in "aeiou":
        c+= string.count(i)
    return(c)
print(vowel_count("dadasuuuuu"))
print("zcsdsfsd".count('d'))