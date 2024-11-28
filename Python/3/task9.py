import math
print('Введите h')
h = int(input())
print('Введите a')
a = int(input())
print('Введите b')
b = int(input())
d = math.ceil((h-a)/(a-b))
if h-a >= 0:
    print (d + 1)
else:
    print(1)