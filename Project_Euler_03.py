for i in range(0,600851475144):
    is_prime =True
    for j in range(2,i):
        if (i%j)==0:
            is_prime = False
        if is_prime:
             if (600851475143%i)==0:
                 print(i)
