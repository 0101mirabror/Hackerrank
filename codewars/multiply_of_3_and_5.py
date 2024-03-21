def solution(numbers):
    c = 0
    if number < 0:
        return 0
    for number in range(numbers+1):
        if number%3==0 and number%5==0:
            c+=number
        elif number%3==0:
            c+=number
        elif number%5==0:
            c+=num
    return c