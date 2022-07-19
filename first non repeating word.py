st = "hello world this is a geeks for geeks"
count = {}
for i in st:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
for i in count:
    if count[i] == 1:
        print(i)
        break
