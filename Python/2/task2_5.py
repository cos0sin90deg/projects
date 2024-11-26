print('Введите первое число')
a = int(input())
print('Введите второе число')
b = int(input())
print('Введите третье число')
c = int(input())
if (a < b) and (b < c):
    print (a)
elif (a < b) and (b > c) and (a < c):
    print (a)
elif (a < b) and (b > c) and (a > c):
    print (c)
elif (a > b) and (b > c):
    print (c)
elif (a > b) and (b < c):
    print (b)
elif (a == b) and (b < c):
    print (a)
elif (a == b) and (b > c):
    print (c)
elif (a > b) and (b == c):
    print (b)
elif (a < b) and (b == c):
    print (a)