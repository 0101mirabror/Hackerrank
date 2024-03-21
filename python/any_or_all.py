n = int(input())
# def is_palindrome(number):
#     return str(number) == str(number)[::-1] 
# def not_palindrome(number):
#     return str(number) != str(number)[::-1] 
numbers = list(map(int, input().split()))
print(numbers)
print(any((lambda x: str(x) == str(x)[::-1])(x) for x in numbers))
# all_positive = all(num>0 for num in list(map(int, input().split())))
print( True if all(num>0 for num in numbers) and any((lambda x: str(x) == str(x)[::-1])(x) for x in numbers) else False)
# lambda n : str(n) == str(n)[::-1]
# print(is_palindrome(5))
# print([i for i in list(map(int, input().split()[:n])) if i>0 and is_palindrome(i)])

# print(True if len([i for i in list(map(int, input().split()[:n])) if i>0 and (lambda n : str(n) == str(n)[::-1])(i)])>0 else False)
# print(False if len(list(filter(((lambda x: str(x) != str(x)[::-1]) and (lambda x: x<0)) or (lambda x: str(x) != str(x)[::-1]) , [i for i in list(map(int, input().split()[:n]))])))>0 else True)
# print(len(list(filter(((lambda x: str(x) != str(x)[::-1] ) and (lambda x: x<0)) or (lambda x: str(x) != str(x)[::-1]) , [i for i in list(map(int, input().split()[:n]))]))))

