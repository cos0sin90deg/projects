n = 1
i = 1
m = 0
while n != 0:
    n = int(input())
    m = n
    if i == 1:
        j = 1
        i = i + 1
        m = n
        k = 1
    else:
        while n == m:
            j = j + 1
            if j - 1 >= k:
            k = j - 1
            n = int(input())
        else:
            j = 1
print(k)