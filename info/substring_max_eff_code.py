s = "bbbbb"
ans = ""
for i in s:
    if i not in ans:
        ans += i
    else:
        id = ans.index(i)
        ans = ans[id+1:] + i
print(len(ans))