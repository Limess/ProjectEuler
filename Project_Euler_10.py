def primalitytest(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for x in range(3, int(n ** 0.5) +1, 2):
        if n % x == 0:
            return False
    return True


number = 1
total  = 2
while number <= 2000000:
    if primalitytest(number):
        total = total + number
    number += 2
print("The Total Sum is: ", total)
