import textwrap
# def wrap(string, max_width):
#     wrapped_text = textwrap.wrap(string, max_width)
#     print(wrapped_text)
#     wrapped_text.pop()
#     print(wrapped_text)
#     for i in wrapped_text:
#         print(i)

# string = input()
# max_width = int(input())
# result = wrap(string, max_width)
# print(result)
# # print(wrap(string, max_width))
 

"2"
def wrap(string, max_width):
    s = ""
    j = 0
    if len(string) % max_width > 0:
        for i in range(len(string)//max_width+1):
            if len(string) // max_width == i: 
                s+=string[-(len(string) % max_width):]
            else:
                s+=string[j:(max_width+j)]+"\n"
                j+=max_width
                # print(s, "s")
                # print(j, "j")
    else:
        for i in range(len(string)//max_width):
            s+=string[j:(max_width+j)]
            j+=max_width
            # print("s", s)
            # print("j", j)
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
