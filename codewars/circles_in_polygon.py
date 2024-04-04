# D = s/(2*tan(pi/n)) #n numberofsides, s=side_length
import math
def func(sides, length):
    return round(length/(math.tan( math.pi/ sides)), 3)
print(math.pi)
print(func(4,5))
print(func(8,9))
print(func(3,4))
print(f'{5:b}', bin(5))