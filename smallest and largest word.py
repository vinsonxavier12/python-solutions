st = "hello world this is a geeks for geeks and myself vinson"
words = st.split()
smallest_word = words[0]
largest_word = words[0]
for i in words:
    if len(i) < len(smallest_word):
        smallest_word = i
    if len(i) > len(largest_word):
        largest_word = i
print("smallest word:", smallest_word)
print("largest word:", largest_word)
