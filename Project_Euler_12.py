from math import sqrt

def d(number):
    t = sqrt(number)
    count = 0
    for i in range (1,int(t)+1):
        if number % i == 0:
            count += 2
        if t == int(t):
            count -= 1
    return count

triangle=1
for i in range (1,1000000):
    if d(i*(i+1)/2)>=500:
        print("The", triangle, "triangle number", "Which is: ", i*(i+1)/2)
        break
    else:
        triangle+=1
            
        
