i = 0
A = input()
A = A.split()
B = []
k = 0
for i in range (len(A)):
    A[i] = int(A[i])
i = 0
while i < len(A):
    if i != 0 and i != len(A)-1:
        if A[i]>A[i-1] and A[i] > A[i+1]:
            k = k + 1
    i = i + 1
print (k)