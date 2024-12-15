n = int(input())
i = 0
s = 0
m = 0
while n != 0:
    if i == 0:
        m = n
        imax = 0
    i = i + 1
    s = s + n
    n = int(input())
    if n > m:
        imax = i - 1
else:
    print (imax)