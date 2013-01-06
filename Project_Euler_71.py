import fractions
import math
temp=0
for d in range (1,1000000 ):
    n=abs(math.floor((3*d-1)/7))
    if fractions.gcd(n,d)==1:
        if temp<fractions.Fraction(n/d)<fractions.Fraction(3/7):
            temp=fractions.Fraction(n/d)
print(fractions.Fraction(temp))
