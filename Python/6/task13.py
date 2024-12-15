n = int(input())
m = 0
i = 1
j = 0
while n != 0:
    if i == 1:
        m = n
        j = 1
    i = i + 1
    n = int(input())
    if n == m:
        j = j + 1
    if n > m:
        m = n
        j = 1
print(j)