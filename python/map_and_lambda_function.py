cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    ls =  [0, 1]
    s = 0
    for i in range(1,n):
        ls.append(ls[i] + ls[i-1])
    return ls[:-1]
print(list(map(cube, fibonacci(int(input())))))