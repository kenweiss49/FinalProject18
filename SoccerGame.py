import random
import time
direction=["right", "middle", "left"]
totalpens=0
userscore=0
compscore=0
print("Welcome to Soccer Shootout Simulator")
userteam = input("What team are you playing for?: ")
print("Good Choice")
time.sleep(1)
teamlist = ["FC Barcelona", "Real Madrid", "Juventus", "Bayern Munich", "Chelsea", "PSG"]
compteam = random.choice(teamlist)
print(f"Welcome to tonight's matchup, {userteam} vs {compteam}. They are playing for the Big Cup!")
time.sleep(3)
print("You have serveral spots to shoot/dive at. Right (right), Middle (middle), Left (left).")
time.sleep(3)
print("Type what is in the parentheses to shoot/dive.")
time.sleep(2)

def userpen():
    global totalpens
    global userscore
    totalpens+=1
    usershot=input("Shoot! : ")
    compdive=random.choice(direction)
    time.sleep(1)
    print("The keeper dives "+str(compdive))
    time.sleep(1)
    if usershot==compdive:
        print("SAVE!")
    else:
        print("GOAL!")
        userscore+=1

def comppen():
    global totalpens
    global compscore
    totalpens+=1
    userdive=input("Dive! : ")
    time.sleep(1)
    compshot=random.choice(direction)
    print("The shooter shot "+str(compshot))
    time.sleep(1)
    if compshot==userdive:
        print("SAVE!")
    else:
        print("GOAL!")
        compscore+=1

def score():
    print(f"Its {userteam}: "+str(userscore)+"")
    print(f"{compteam}: "+str(compscore)+"")

def finalscore():
    print(f"Final- {userteam}: "+str(userscore)+"")
    print(f"{compteam}: "+str(compscore)+"")
    if userscore>compscore:
        print(f"You won! {userteam} are the Big Cup Champions!")
    elif userscore<compscore:
        print(f"You lost! {compteam} are the Big Cup Champions!")

while totalpens<10:
    userpen()
    comppen()
    score()
finalscore()



