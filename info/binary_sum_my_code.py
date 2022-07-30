t = int(input())
a = []
for i in range(t):
    a.append(input().split())
b = []
c = []
d = []
for i in a:
    for j in range(len(i)):
        c.append(int(i[j], 2))
    b.append([i for i in c])
    c.clear()
for i in b:
    d.append(sum(i))
print(bin(max(d))[2:])