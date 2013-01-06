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
primes = 1
switch = 1
while switch == 1:
    if primalitytest(number):
        primes += 1
        
    if primes == 10001:
        print("The 100001st prime is: ", number)
        switch = 0
    number += 2
