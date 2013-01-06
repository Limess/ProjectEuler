def is_palindromic(number):
    string=str(number)
    if number == int(string[::-1]):
        return True
    else:
        return
Temp=0
for i in range (100,1000):
    for j in range(i,1000):
        if is_palindromic(i*j)==True:
            if (i*j)>=Temp:
                Temp=(i*j)
                print("i is", i, "j is", j , "number", Temp)

