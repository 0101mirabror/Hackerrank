ls = [1,2,3,5,6,8,9,7,8]
import random
t = True
tar = 16
while t:
    random_element1 = random.choice(ls)
    index1 = ls.index(random_element1)
    random_element2 = random.choice(ls)
    index2 = ls.index(random_element2)
    if (random_element1 + random_element2 == tar) and (index1 != index2):
        print([index1, index2])
        t = False


# tar = 16
# count_list = len(ls)
# print(ls[(0-0)])
# emp = []
# t = True
# k = count_list
# while t:
#     print(k)          
#     x = [[ls[i], ls(count_list-k)] for i in range(count_list) if (ls[(count_list-k)] + ls[i]) == tar]
#     emp = emp + x
#     k=k-1
#     if k == 0:
#         t = False
#         break
# print(emp)
        
    



# print(k)
# if 1 in 4:
    # print(True)