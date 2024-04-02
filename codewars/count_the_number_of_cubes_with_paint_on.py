def count_squares(cuts):
    return 2*((cuts+1)**2) + 2*(cuts-1)*(cuts-1)+ 2*(cuts-1)*(cuts+1)

print(count_squares(2))
print(count_squares(3))
print(count_squares(4))