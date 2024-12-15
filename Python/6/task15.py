A = float(input())
a = 0
b = 1
i = 0
c = -1
while i < A+3:
    if i == 0 or i == 1:
        b = i
        i = i + 1
    else:
        i = i + 1
        a, b = b, a+b
    if b == A:
        c = 1
        break
    if b > A:
        print (-1)
        break
else:
    print (-1)
if c == 1:
    print(i-1)