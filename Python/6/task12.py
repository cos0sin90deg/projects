n = int(input())
m = 0
i = 1
z = 0
while n != 0:
    if i == 1:
        m = n
    if i == 2:
        if m > n:
            m, z = n, m
        else:
            m, z = m, n
    n = int(input())
    i = i + 1
    if i > 2:
        if n < m:
            m, z = m, z
        if n > m:
            if m < z < n:
                m, z = z, n
            if m < n < z:
                m, z = n, z
print(m)