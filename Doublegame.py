import random
import string
flag=0
score=0
while(flag==0):
    l1=list(string.ascii_letters)
    s1 = random.sample(l1, k=8)
    for j in range(0,8):
        l1.remove(s1[j])
    r=random.sample(s1,k=1)
    s2=random.sample(l1,k=7)
    s2.extend(r)
    random.shuffle(s2)
    print(s1)
    print(s2)
    print("Spot the similar symbol")
    t=str(input())
    check=(t in s1) and (t in s2)
    if check is True:
        score=score+1
        print("Correct")    
    else :
        print("Wrong Answer")
        s3=set(s1)
        s4=set(s2)
        print("common symbol is",(s3.intersection(s4)))
    print("Do you wish to continue(y/n)?")
    wish=input()
    if(wish != 'y'):
        flag=1
        print("Thank you! Your score is ", score," points")
