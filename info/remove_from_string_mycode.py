num = "1231"
rem = '1'
res = []
s = ""
for i in range(len(num)):
    if num[i] == rem:
        s = num[:i] + num[i + 1:]
        res.append(int(s))
print(res)
print(max(res))