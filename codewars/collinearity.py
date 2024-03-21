def collinearity(x1, y1, x2, y2):
    if (x1 == 0 and y1 ==0) or (x2 == 0 and y2 ==0): #if x1 is 0, then x2 is also 0, and reversed
        return True
    elif y1 != 0 and y2 != 0 and x1/y1 == x2/y2:
        return True
    elif x1 != 0 and x2 != 0 and y1/x1 == y2/x2:
        return True
    else:
        return False
print(collinearity(0,0,0,0))
print(collinearity(1,1,1,1))
print(collinearity(1,2,2,4))
print(collinearity(0,1,0,2))
# 
# def collinearity(x1, y1, x2, y2):
    # return x1 * y2 == x2 * y1