A = input()
A = A.split()
m = 0
for i in range (len(A)):
    A[i] = int(A[i])
    i = i + 1
i = 0
j = 0
while i < len(A):
    if (A[i] in A[i+1:len(A)]) == False:
        print(A[i])
    i = i + 1
print(m)