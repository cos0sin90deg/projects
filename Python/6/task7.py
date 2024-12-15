n = int(input())
i = 0
s = 0
while n != 0:
    i = i + 1
    s = s + n
    n = int(input())
else:
    print(s/i)