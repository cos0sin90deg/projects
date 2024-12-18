i = 0
A = input()
A = A.split()
B = []
k = 0
m = 0
for i in range (len(A)):
    A[i] = int(A[i])
m = max(A)
k = A.index(m)
print (m)
print (k)