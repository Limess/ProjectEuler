maxcount=0
a=0
for n in range (1,1000000):
    a=n
    count=0
    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
        count=count+1    
    if count>=maxcount:
        maxcount=count
        print(["starting number"],[a],["maxcount"],maxcount)
print(["maxcount"],maxcount)
