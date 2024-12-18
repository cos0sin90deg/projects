A = input()
A = A.split()
m = 0
for i in range (len(A)):
    A[i] = int(A[i])
    i = i + 1
i = 0
j = 0
while i < len(A) - 1:
    k = A[i]
    while j < len(A):
        if j == len(A) - 1:
            break
        B = A[j+1:len(A)]
        if (k in B) == True:
            m = m + 1
            j = B.index(k)
            j = j + 1
        j = j + 1
    i = i + 1
print(m)