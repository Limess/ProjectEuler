from sys import argv

script, from_file = argv

print("Importing data from file %s \n" %from_file)

f = open(from_file, "r")

tally = 0

for i in f.readlines():
    ipl = i.replace("\n", "")
    if ipl.isdigit():
        number = int(ipl)
        tally += number
    else:
        print("The variable ipl contains no digit")
        
f.close()
print("The tally is: ", tally)
