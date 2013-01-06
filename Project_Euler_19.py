sun=0
def  is_sun(day):
    if day%7==5:
      return True
        
year=1901
day=0
   
while year<=2000:
    if year%4==0 and year%100!=0:
        day+=31 #January
        if is_sun(day):
            sun+=1
        day+=29 #February
        if is_sun(day):
            sun+=1
        day+=31 #March
        if is_sun(day):
            sun+=1
        day+=30 #April
        if is_sun(day):
            sun+=1
        day+=31 #May        
        if is_sun(day):
            sun+=1
        day+=30 #June
        if is_sun(day):
            sun+=1
        day+=31 #July
        if is_sun(day):
            sun+=1
        day+=31 #August
        if is_sun(day):
            sun+=1
        day+=30 #September
        if is_sun(day):
            sun+=1
        day+=31 #October
        if is_sun(day):
            sun+=1
        day+=30 #November    
        if is_sun(day):
            sun+=1
        day+=31 #December
        if is_sun(day):
            sun+=1
    else:
        day+=31 #January
        if is_sun(day):
            sun+=1
        day+=28 #February
        if is_sun(day):
            sun+=1
        day+=31 #March
        if is_sun(day):
            sun+=1
        day+=30 #April
        if is_sun(day):
            sun+=1
        day+=31 #May        
        if is_sun(day):
            sun+=1
        day+=30 #June
        if is_sun(day):
            sun+=1
        day+=31 #July
        if is_sun(day):
            sun+=1
        day+=31 #August
        if is_sun(day):
            sun+=1
        day+=30 #September
        if is_sun(day):
            sun+=1
        day+=31 #October
        if is_sun(day):
            sun+=1
        day+=30 #November    
        if is_sun(day):
            sun+=1
        day+=31 #December
        if is_sun(day):
            sun+=1
    year+=1
print("The number of sundays between 1 Jan 1901 and 31 Dec 2000 is: ", sun)
