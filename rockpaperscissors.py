import random
store1 = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
store2 = random.randint(0, 2)
if store1<3 or store1>=0:
    if store1==store2:
        print("It's a draw, try again!")
    elif store1==0 and store2==2:
        print("Computer chose scissors, you won!")
    elif store1==2 and store2==1:
        print("Computer chose paper, you won!")            
    elif store1==1 and store2==0:
        print("Computer chose rock, you won!")
    else:
        print("You lost")         
else:
    print("Invalid number, please try again.")        