total = 0
number = str(2 ** 1000)
print("2^1000 is: ", number)

for i in range (0, len(number)):
    total = total + int(number[i])
print("The total is:", total)
