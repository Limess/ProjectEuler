a = sum([len("one"),len("two"),len("three"),len("four"),len("five"),len("six"),len("seven"),len("eight"),len("nine")]) #1 to 9
b = sum([len("ten"),len("eleven"),len("twelve"),len("thirteen"),len("fourteen"),len("fifteen"),len("sixteen"),len("seventeen"),len("eighteen"),len("nineteen")]) #10 to 19
c = sum([len("twenty"),len("thirty"),len("forty"),len("fifty"),len("sixty"),len("seventy"),len("eighty"),len("ninety")]) #20 to 90
l =  a*9*10 #1-99,101-199,201-299,301-399,401-499,501-599,601-699,701-799,801-899,901-999
l += b*10 #teens in each block
l += c*10*10 #tens in each block
l += a*100
l += len("hundred")*900 
l += len("onethousand") #1000
l += len("and")*99*9 #and for 101-999 excluding hundreds

print("The total is: ", l)
