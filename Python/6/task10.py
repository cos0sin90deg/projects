n = int(input())
imax = -1
while n != 0:
    if n%2 == 0 and imax != -1:
        imax = imax + 1
    if imax == -1 and n%2 == 0:
        imax = 1
    n = int(input())
if imax == -1:
    print ('Чётных чисел нет')
else:
    print (imax)