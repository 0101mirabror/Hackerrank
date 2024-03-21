# n = int(input())
# for i in range(1 ,n):
#     print(int(f"{i}"*i)) # cant be string


'3'
 
# def series_sum(x, n):
#     total = 0
#     power = x - 1

#     for i in range(n):
#         term = x * (10 ** power)
#         total += term
#         power -= 1

#     return total
# # print(series_sum(3,3))
# n = int(input())
# for i in range(1, n):
#     print(series_sum(i, i))
    
'4'
def series_sum(x, n):
    return sum(x * (10 ** (x - 1 - i)) for i in range(n))
