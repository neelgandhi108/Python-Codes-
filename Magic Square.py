def magic_square(n):
    magicSquare=[]    # defining a variable magic square
    for rows in range(n):
        list=[] # defining the list so that whenever loops initiated a new list created for each row
    for cols in range(n):
        list.append(0) # whenever cols loop will be passed rows will be appended by values in list 
    magicSquare.append(list)


# fIXING THE 1 IN MAGIC SQUARE USING FORMULA(condition 1)
    rows=n//2
    cols=n-1
# Assining matrix as user input no itnot that no 
    matrix=n*n
    count=1 # element variable , as soon as elements will be assinged count variable will increase to next variable Util unless all elements are assinged

 #Condition 5  
    while (count<=matrix):
        if(rows==  -1 and cols== n):  
            cols = n-2 
            rows = 0
# Condition 3
        else:
            if(cols==n):  #Coloum values exceding
                cols=0

            if(rows<0):#rows value becomes -1
                rows=n-1
#condition 4
        if(magicSquare[rows][cols]!= 0): #if has some elements in location
            cols = cols-2 
            rows = rows+1
            continue   # skip what ever written below this and go back to while loop to check if a condtion said above repeats and do accordingly, if not:
        else:
            magicSquare[rows][cols] = count
            count+=1  #increment the count variable 
#condition 2(for second element)
        rows = rows-1 
        cols = cols

# printing magicSquare

        for rows in range(n):
            for cols in range(n):
             print(magicSquare[rows][cols], end = " ")
             print()

magic_square(3)
