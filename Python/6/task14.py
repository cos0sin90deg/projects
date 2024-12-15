n = int(input())
a = 0
b = 1
i = 0
while i < n+1:
    if i == 0 or i == 1:
        b = i
        i = i + 1
    else:
        i = i + 1
        a, b = b, a+b
print(b)