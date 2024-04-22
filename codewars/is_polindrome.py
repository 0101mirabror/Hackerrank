def is_palindrome(s:str):
    return s[:len(s)//2].lower() == s[len(s)//2:].lower()[::-1] if len(s)%2==0 else s[:len(s)//2+1].lower() == s[len(s)//2:].lower()[::-1] 
print(is_palindrome('a'))
print(is_palindrome('aba'))
print(is_palindrome('ABba'))