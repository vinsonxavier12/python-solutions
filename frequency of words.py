st = "hello world this is a geeks for geeks"
freq = {}
for word in st:
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1
print(freq)
