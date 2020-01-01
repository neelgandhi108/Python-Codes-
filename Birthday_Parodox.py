import DateTime
import random

birthday=[]  #creating list with []
i=0 # assining a var for loop
while(i<50):  # running a while loop until 1<50
    year=random.randint(1877,2019) # becuase macx person was 142 yrs
# leap year program
#(years)
    if(year%4==0 and year%100 !=0 or year%400==0):
        leap=1
    else:
        leap=0
#months
        month=random.randint(1,12)
#day<nested if else>
        if(month==2 and leap==1): # for days in feb , leap year
            day=random.randint(1,29)
        elif(month==2 and leap==0):#for days in feb , not leap year
            day=random.randint(1,28) 
        elif(month==7 or month==8):#for days in july and aug
            day=random.randint(1,31)
        elif(month%2!=0 and month<7):#for days in  Aug, Oct and Dec
            day=random.randint(1,31)
        elif(month%2==0 and month>7 and month<12):
            day=random.randint(1,31)
        else:
            day=random.randint(1,30) #for days in Jan, March , May, July
            
# printing in the specified format

        dd=datetime.date(year,month, day) # setting variable dd for right format using date time library
        day_of_year=dd.timetuple().tm_yday # prints day of year
        i=1+1 # incrementing loop and adding new element
        birthday.append(day_of_year) # appending to bithday list
        
birthday.sort() #sorting list
i=0 # intiating variable as 0
while(i<50): #printing 50 people values in a row order
    print(birthday[i])
    i=i+1
