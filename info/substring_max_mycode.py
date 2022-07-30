s = "bbbbbb"

b = []
x = ""
res = []
prev_index = -1

for i in range(len(s)):
    for j in range(i, len(s)):
        if s[j] not in b and j - prev_index == 1:
            b.append(s[j])
            x += s[j]
            prev_index = j
    res.append(x)
    b = []
    x = ""
    prev_index = i
print(res)
ixs = [len(i) for i in res]
print(max(ixs))