st = "hello world this is a geeks for geeks"
st, result = st.title(), ""
words = st.split()
for word in words:
    result += word[:-1] + word[-1].upper() + ' '
print(result)
