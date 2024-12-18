i = 0
k = 0
A = input()
A = A.split()
for i in range (len(A)):
    A[i] = int(A[i])
    i = i + 1
i = 0
m = max(A)
mi = A.index(m)
l = min(A)
li = A.index(l)
A[mi] = l
A[li] = m
print (A)