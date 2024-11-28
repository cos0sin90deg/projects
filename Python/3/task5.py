import math
print('Введите номер урока')
a = int(input())
b = 9*60 + 25*(a // 2) + 5*(a % 2) + 45*a
print(b // 60,' ', b % 60)