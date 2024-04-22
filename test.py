x = 0.99365
a = 0
b = 1
# for i in range(365):
#     b = x*0.01
#     x += b
#     print(x)

for i in range(365):
    b = x*0.01
    x -= b
    print(x)