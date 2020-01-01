#List for door and goats door
doors=[0]*3
goat_doors=[0]*2
#counter to track wether to swap or not
swap=0
dont_swap=0
# track
track=0
while(track<3): #looping till 3 , ends when 3 rounds complete
#Importing random variables from range 0,2 as 3 will count as 3 in index
    import random
    x=random.randint(0,2) # xth door will have bmw
#doors configuaration
    doors[x]="BMW" 
#goat door
    for i in range(0,3): # 0,3 is taken in account as it will exclude 3rd door as it will be 4th door
        if (i==x): # if given door is bmw(xth) door
            continue   # go to the strart of loop and increment i
        else:
            doors[i]="goat" #door at ith position is goat door
            goat_doors.append(i) #so append door to particular index i here
# let user input the choice
    choice=int(input("Please Enter Your Choice: "))
# open the door
    door_open=random.choice(goat_doors) # here only those doors will open which has a goat , if it has prize game will start again
#door opened should not be the same made by the participants
    while(door_open==choice):
        door_open=random.choice(goat_doors)
#after 1st time door opens , user given choice to swap   
    choice1=input("Do You Want To Swap Y/N: ")
# if player swaps and doors are same as goat door then swap it as one goat door is already opened and 2nd one has a goat , but if player sap then he will get BMW
    if(choice1=="Y"):
        if (doors[choice]=='Goat'):
            print("Congrats You Won") # he wins
            swap=swap+1 # swap counter is incremented
        else: # if player selected BMW and swap he looses
            print("Sorry Better Luck Next Time!") 
    else:# if the player chooses not to swap and he still continues with the goat he loses if not he swaps at second one he wins
        if(doors[choice=='Goat']):
            print("You Lost")
        else:
            print("Congrats, You Won!")
            dont_swap=dont_swap+1
            
    track=track+1    #increment the loop to end
    
print(swap) # print no of swap wins
print(dont_swap) #print no of don't swap win
