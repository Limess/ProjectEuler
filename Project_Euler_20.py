import math
total = 0
number = str(math.factorial(100))
print("100! is: ", number)

for i in range (0, len(number)):
    total = total + int(number[i])
print("The total is:", total)
