n=1
k=2520
while n==1:
    if all(k%j==0 for j in range(1,20)):
        n=2
        print("Answer is", k)
    else:
        k=k+2520
