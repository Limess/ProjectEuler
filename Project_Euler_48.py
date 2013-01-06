total = 0
for i in range (1,1000):
    total = (total + i ** i)
string = str(total)
print(string[-10:])
