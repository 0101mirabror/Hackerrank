def solve(s):
    cap_text = [i.capitalize()  for i in s.split(" ")]
    print(cap_text)
    t = cap_text[0]
    for i in range(1, len(cap_text)):
        t+=" " + cap_text[i]
    # t = ""
    # for i in cap_text:
    #     print(i)
    #     t.join(f"{i}")
    return t
print(solve(input()))