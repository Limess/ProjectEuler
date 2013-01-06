from math import sqrt

def d(number):
    s = 1
    t = sqrt(number)
    for i in range (2,int(t)+1):
        if number % i == 0:
            s += i + number/i
        if t == int(t):
            s -= t
    return s



count=0
for y in range (2,10000):
     d_y = d(y)
     if d(y) > y and d(d_y) == y:
         count += d_y + y

print("The answer is: ", count)
