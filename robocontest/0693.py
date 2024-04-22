n = int(input())
st = input()
word  = [ x[::-1] for x in st.split() if len(x) > n ]
# word = list(map(lambda x: x[::-1] if len(x) > n else None , st.split()))
print(" ".join(word))