n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

count = 0
a.sort()
while len(a) != 0:
    if a[0] != a[-1]:
        a.remove(a[0])
        a.remove(a[-1])
    else:
        a.remove(a[0])
    count += 1
print(count)