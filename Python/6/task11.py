n = int(input())
imax = -1
m = 'начало'
while n != 0:
    if m != 'начало':
        if n > m and imax != -1:
            imax = imax + 1
        if n > m and imax == -1:
            imax = 1
    m = n
    n = int(input())
if imax == -1:
    print(0)
else:
    print (imax)