print('Введите первое число')
a = int(input())
print('Введите второе число')
b = int(input())
print('Введите третье число')
c = int(input())
if (a == b) and (b == c):
    print (3)
elif ((a == b) and (b!= c)) or ((a != b) and (b == c)) or ((a == c) and (a != b)):
    print (2)
else:
    print (0)