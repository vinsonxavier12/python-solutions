t = int(input())
res = 0
for i in range(t):
    A, B = input().split()
    a = int(A, 2)
    b = int(B, 2)
    s = a + b
    if s > res:
        res = s
print(bin(res)[2:])