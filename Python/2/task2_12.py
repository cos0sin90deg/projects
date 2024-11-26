print('Введите n')
n = int(input())
print('Введите m')
m = int(input())
print('Введите k')
k = int(input())
if (k % n == 0) and (m >= k / n):
    print ('YES')
elif (k % m == 0) and (n >= k / m):
    print ('YES')
else:
    print ('NO')