"""
Given an integer x, return true if x is a 
palindrome, and false otherwise.
"""
 
 

def checkPolindrom(num):
    a = num
    b = 0
    c1 = 0
    while a > 0:
        r = a % 10
        a = a//10
        b = 10*b + r
    if num == b:
        return True
    else:
        return False


print(checkPolindrom(88888))