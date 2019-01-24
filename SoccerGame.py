import random
import time
direction=["right", "middle", "left"] #valid directions the user can shoot/dive
totalpens=0
userpen=0
comppen=0
userscore=0
compscore=0 #set all variables equal to 0 at the beginning of the game
print("Welcome to Soccer Shootout Simulator!")
time.sleep(1)
userteam = input("What team are you playing for?: ") #user input of their team choice for the game
print("Good Choice")
time.sleep(1)
teamlist = ["FC Barcelona", "Real Madrid", "Juventus", "Bayern Munich", "Chelsea", "PSG", "Atletico Madrid", "Manchester United", "Manchester City", "Liverpool FC", "Arsenal", "Tottenham Hotspur", "Borussia Dortmund", "AC Milan", "Inter Milan", "FC Porto", "Ajax", "Schalke", "Galatasaray", "Tigres"]
compteam = random.choice(teamlist) #computer team is randomly generated
print(f"Welcome to tonight's matchup, {userteam} vs {compteam}. They are playing for the Big Cup!")
time.sleep(3)
print("You have several spots to shoot/dive at. Right (right), Middle (middle), Left (left).")
time.sleep(3)
print("Choose a spot and type what is in the parentheses above exactly to shoot/dive. If you dont, you automatically miss the shot.")
time.sleep(5) #Welcoming/Information stuff
commentaryscore = ["What a strike!", "Keeper had no chance.", "Off the bar and in.", "It's a wondergoal!", "Off the boot, in the back of the net.", "Oh my word, the curve.", "Just enough power behind that one.", "An absolute stunner!", "The crowd is cheering after that one.", "The manager is happy with that one"]
commentarysave = ["What a save!", "Keeper got a hand on it.", "Had to really stretch there", "Wonderful save!", "Off the gloves and out.", "Not enough to get past", "Power on the shot, but stopped.", "Wacked out of danger!", "Crowd is in disbelief.", "Manager would've liked it to get past the keeper."]
commentarymiss = ["My word, right over the bar!", "No chance of that going in.", "Missed it wide.", "Really had anywhere else to shot.", "Dissapointing, really.", "Shoulda hit the target."]
#commentary for the game

def userpen(): #how the users penalty works
    global totalpens
    global userscore
    global commentaryscore
    global commentarysave
    global commentarymiss
    commentaryscore1=random.choice(commentaryscore)
    commentarysave1=random.choice(commentarysave)
    commentarymiss1=random.choice(commentarymiss) #getting random commentary ready
    userpen==0
    totalpens+=1 #Add 1 to total penalties
    usershot=input("Shoot! : ")
    compdive=random.choice(direction) #random computer direction
    time.sleep(1)
    print("The keeper dives "+str(compdive))
    time.sleep(1)
    if usershot==compdive: #stuff for saved shot
        print("SAVE!")
        time.sleep(1)
        print((commentarysave1)) #prints commentary
    elif usershot=="left" and compdive=="right":
        print("GOAL!")
        time.sleep(1)
        print((commentaryscore1))
        userscore+=1
    elif usershot=="left" and compdive=="middle":
        print("GOAL!")
        time.sleep(1)
        print((commentaryscore1))
        userscore+=1
    elif usershot=="middle" and compdive=="right":
        print("GOAL!")
        time.sleep(1)
        print((commentaryscore1))
        userscore+=1
    elif usershot=="middle" and compdive=="left":
        print("GOAL!")
        time.sleep(1)
        print((commentaryscore1))
        userscore+=1
    elif usershot=="right" and compdive=="middle":
        print("GOAL!")
        time.sleep(1)
        print((commentaryscore1))
        userscore+=1
    elif usershot=="right" and compdive=="left": #every valid but not equal shot attempt results in a goal
        print("GOAL!")
        time.sleep(1)
        print((commentaryscore1))
        userscore+=1 #add 1 to userscore
    elif usershot=="right" and compdive=="right":
        print("SAVE!")
        time.sleep(1)
        print((commentaryscore1))
    elif usershot=="middle" and compdive=="middle":
        print("SAVE!")
        time.sleep(1)
        print((commentaryscore1))
    elif usershot=="left" and compdive=="left": #every equal shot attempt results in a saved shot
        print("SAVE!")
        time.sleep(1)
        print((commentaryscore1))
    else:
        print("MISS!") #if input is not a valid direction, you miss
        time.sleep(1)
        print((commentarymiss1))

def comppen():
    global totalpens
    global compscore
    global commentaryscore
    global commentarysave
    global commentarymiss
    commentaryscore1=random.choice(commentaryscore)
    commentarysave1=random.choice(commentarysave)
    comppen==0
    totalpens+=1 #adds 1 to total overall penalties
    userdive=input("Dive! : ")
    time.sleep(1)
    compshot=random.choice(direction)
    print("The shooter shot "+str(compshot))
    time.sleep(1)
    if compshot=="left" and userdive=="left":
        print("SAVE!")
        time.sleep(1)
        print((commentarysave1))
    elif compshot=="right" and userdive=="right":
        print("SAVE!")
        time.sleep(1)
        print((commentarysave1))
    elif compshot=="middle" and userdive=="middle": #every equal save attempt is a save
        print("SAVE!")
        time.sleep(1)
        print((commentarysave1))
    else:
        print("GOAL!") #everything else is a computer goal
        compscore+=1 #adds 1 to computer score.
        time.sleep(1)
        print((commentaryscore1))

def ot(): #if both teams have an equal score at the end of the 5 rounds
    global totalpens
    global userscore
    global compscore
    time.sleep(1)
    print(f"A tie? Not tonight. One final shot to deside the winner. A goal and {userteam} wins, a save and {compteam} wins!")
    time.sleep(3)
    usershot=input("Shoot! : ")
    compdive=random.choice(direction)
    time.sleep(1)
    print("The keeper dives "+str(compdive))
    time.sleep(1)
    if usershot==compdive: #saved shot
        print("SAVE!")
        compscore+=1
    elif usershot=="left" and compdive=="right":
        print("GOAL!")
        userscore+=1
    elif usershot=="left" and compdive=="middle":
        print("GOAL!")
        userscore+=1
    elif usershot=="middle" and compdive=="right":
        print("GOAL!")
        userscore+=1
    elif usershot=="middle" and compdive=="left":
        print("GOAL!")
        userscore+=1
    elif usershot=="right" and compdive=="middle":
        print("GOAL!")
        userscore+=1
    elif usershot=="right" and compdive=="left": #All types of goals
        print("GOAL!")
        userscore+=1
    elif usershot=="right" and compdive=="right":
        print("SAVE!")
    elif usershot=="middle" and compdive=="middle":
        print("SAVE!")
    elif usershot=="left" and compdive=="left": #All types of saves
        print("SAVE!")
    else:
        print("MISS!")

def score(): #displays score at end of each shot
    time.sleep(1)
    print(f"Its {userteam}: "+str(userscore)+"")
    print(f"{compteam}: "+str(compscore)+"")

def finalscore(): #displays when there is a winner
    time.sleep(1)
    print(f"Final- {userteam}: "+str(userscore)+"")
    print(f"{compteam}: "+str(compscore)+"")
    if userscore>compscore:
        print(f"You won! {userteam} are the Big Cup Champions!")
    elif userscore<compscore:
        print(f"You lost! {compteam} are the Big Cup Champions!")

def gameplay(): #defines how gameplay runs
    while totalpens<10:
        userpen()
        score()
        comppen()
        score()
    while totalpens<=10 and userscore==compscore:
        ot()
    finalscore()

gameplay() #actually runs gameplay
