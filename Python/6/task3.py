n = int(input())
i = 1
j = 0
while i < n:
    if i*2 > n:
        continue
    else:
        i = i*2
        j = j+1
else:
    print(i)
    print(j)