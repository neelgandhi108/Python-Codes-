import random
#creating a list of movies
movies=['anbe sivan','nayakan','wanted','vikram vedha','black fiday','dangal','manichithrathazhu','gol maal','terminator','anand']
def create_question(movie):#defining question function
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==" ":
            temp.append(" ")
        else:
            temp.append("*")
    qn=" ".join(str(x) for x in temp)
    return qn
def is_present(letter,movie):#defining the function-(if the guessed letter is present)
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True
def unlock(qn,movie,letter):#unlocking the letters
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if ref[i]==" " or ref[i]==letter:
            temp.append(ref[i])
        else:
            if qn_list[i]=="*":
                temp.append("*")
            else:
                temp.append(ref[i])
    qn_new=" ".join(str(x) for x in temp)
    return qn_new

#defining guess the movie-game function
def play():#getting the player names as input
    p1name=input("player 1: please enter your name:")
    p2name=input("player 2: please enter your name:")
    pp1=0 #initialising the required variables
    #points of the player
    pp2=0
    #players-turn
    turn=0
    #if the game is to be continued
    willing=True
    while willing:
        #checking if the turn if odd or even
        if turn%2==0:
            #player 1
            print(p1name,"Your turn")
            #picking a random movie
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("Enter a letter:")
                if(is_present(letter,picked_movie)):
                    #unlocking the blanks
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("Press 1 to guess the movie or 2 to unlock another letter:"))
                    if d==1:
                        ans=input("Your answer:")
                        if ans==picked_movie:
                            pp1=pp1+1
                            print("Correct")
                            not_said=False
                            print(p1name,"Your score:",pp1)
                        else:
                            print("Wrong answer, Try again:")       
                else:
                    print(letter,"not found")
            c=input("Press 1 to continue or 0 to quit")
            if c==0:
                print(p1name,"Your Score:",pp1)
                print(p2name,"Your Score:",pp2)
                print("Thanks for playing")
                print(" Have a great day!!!!")
                willing=False
        else:
            #player 2
            print(p1name,"Your turn")
            #picking a random movie
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("Enter a letter:")
                if(is_present(letter,picked_movie)):
                    #unlocking the blanks
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("Press 1 to guess the movie or 2 to unlock another letter:"))
                    if d==1:
                        ans=input("Your answer:")
                        if ans==picked_movie:
                            pp2=pp2+1
                            print("Correct")
                            not_said=False
                            print(p2name,"Your score:",pp2)
                        else:
                            print("Wrong answer, Try again:")
                else:
                    print(letter,"not found")
            c=input("Press 1 to continue or 0 to quit")
            if c==0:
                print(p1name,"Your Score:",pp1)
                print(p2name,"Your Score:",pp2)
                print("Thanks for playing")
                print(" Have a great day!!!!")
                willing=False
        #incrmenting the turn
            turn=turn+1
#calling the function-play
play()
