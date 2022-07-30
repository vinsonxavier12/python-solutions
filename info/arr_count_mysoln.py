arr = [2, 2, 2]
count = 0
i = 0
while len(arr) > 1 and i < len(arr):
    x = arr[0]
    y = arr[-1]
    if y == x:
        y = arr[i]
    if x != y:
        arr.remove(x)
        arr.remove(y)
        count += 1
    i += 1
while arr:
    x = arr[0]
    arr.remove(x)
    count += 1
print(count)
