# This program calculates the sum of even terms of the Fibonacci sequence which do not exceed 4 million
a = 1
b = 1
c = 0
term = 2
while len(str(c))!=1000:
    term+=1
    if a>b:
        c = a + b
        b = c
    else:
        c = a + b
        a = c
print("Term: ", term, "Value: ", c)
