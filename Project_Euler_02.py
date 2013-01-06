# This program calculates the sum of even terms of the Fibonacci sequence which do not exceed 4 million
a = 0
b = 1
c = 0
while b <=(4*(10**6)):
    old_a = a    
    a = b
    b = old_a + b
    if b%2==0:
        c=c+b
print(c)
