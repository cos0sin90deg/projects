from math import sqrt
x = 1
i = 0
s = 0
sq = 0
while x != 0:
    x = int(input())
    if x != 0:
        s = s + x
        sq = sq + x**2
        i = i + 1
print (sqrt(((sq - 2*(s**2)/i + (s**2)/i)/(i-1))))
