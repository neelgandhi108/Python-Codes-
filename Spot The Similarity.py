import string
import random
symbols=[]
symbols.append((string.ascii_letters))
Card1=[0]*5
Card2=[0]*5
pos1=random.randint(0,4)
pos2=random.randint(0,4)
print("The selected first position is : ",pos1)
print("The selected Second position is : ",pos2)

#let's now choose a symbol for matching and removing it from list
samesymbol=random.choice(symbols)
symbols. remove(samesymbol)

#if pos1 and pos2 are same symbol positions in card 1 and 2
if(pos1==pos2):
    Card2[pos1]=samesymbol
    Card1[pos1]=samesymbol
else:
    Card1[pos1]=samesymbol
    Card2[pos2]=samesymbol
    Card1[pos2]=random.choice(symbols)
    symbols. remove(card1[pos2])
    Card2[pos1]=random.choice(symbols)
    symbols.remove(Card2[pos1])
#making a variable to iterate over loop
i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
       alphabet1=random.choice(symbols)
       symbols.remove(alphabet1)
       alphabet2=random.choice(symbols)
       symbols.remove(alphabet2)
       Card1[i]=alphabet1
       Card2[i]=alphabet2
    i=i+1
print(Card1)
print(Card2)
ch=input("Spot the similar symbol:")
if(ch==samesymbol):
    print("Right")
else:
    print("Wrong")
