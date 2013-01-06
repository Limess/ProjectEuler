import math
for a in range (1,1000):
    for b in range (a+1, 1000):
        c = math.sqrt(a ** 2 + b ** 2)
        if (1000 == a + b + c):
            print(a*b*c)
