input = [
            [ 0, 1, 2, 3, 4 ],
            [ 10,11,12,13,14 ],
            [ 20,21,22,23,24 ],
            [ 30,31,32,33,34 ]
] 
def to_csv_text(array):
    # st = ''
    # for i in array:
    #     st+=str(i).replace('[', '').replace(']', '').replace(' ', '') + '\n'
    return ''.join(str(i).replace('[', '').replace(']', '').replace(' ', '') + '\n' for i in array)[:-1]
    # good luck
print(to_csv_text(input))