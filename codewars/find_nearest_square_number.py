import math
def find_nearest(n):
    if math.sqrt(n) == int(math.sqrt(n)) :
        return n
    else:

        a = int(math.sqrt(n)) + 1
        b = int(math.sqrt(n)) 
        print(a,b)
        if a**2 - n < n - b**2:
            return a**2
        return b**2
        
        
print(find_nearest(111))
print(find_nearest(64))
print(find_nearest(10))
print(find_nearest(2))
        
# best
# def nearest_sq(n):
    # return round(n ** 0.5) ** 2
 
 