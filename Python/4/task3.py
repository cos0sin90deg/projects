print('Введите A')
A = int(input())
print('Введите B')
B = int(input())
for i in range (1, (A-B + B%2 + A%2)//2 + 1):
    n = A + A%2 - 1 - 2*(i - 1)
    print(n)