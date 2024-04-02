def draw_stairs(n):
    k = ''
    for i in range(1, n+1):
        k += "I\n"+i*" "
    return k[:-(n+1)]
print(draw_stairs(7))