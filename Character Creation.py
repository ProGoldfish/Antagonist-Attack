import random, winsound, os
from Save import SaveData
seed = []
savedata = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def NewPage():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

username = ""

winsound.PlaySound("Sounds/careless.wav", winsound.SND_LOOP + winsound.SND_ASYNC)

for i in range(200):
    seed.append(random.randint(0,9))

done = "n"
while done == "n":
    NewPage()
    while len(username) < 1 or len(username) > 15 or any(ext in username for ext in ["0","1","2","3","4","5","6","7","8","9"," "]):
        username = input("Please enter a username that you will remember: (no numbers or spaces - usernames are not case sensitive)\n> ").capitalize()

    while savedata[0] not in ["1","2","3"]:
        savedata[0] = input("\nChoose a class:\nArcher (1)\nWarrior (2)\nAlchemist (3)\n> ")
    if savedata[0] == "1":
        playerhp = 100
        print("\nYou have chosen Archer!\n\nA ranger able to make full use of the long range weapons.\nYou shoot down your enemies but be careful not to get hit!\n\nHealth: 100\nMaximum Damage: 25\nMinimum Damage: 20\nArmour: 1") 
    if savedata[0] == "2":
        playerhp = 125
        print("\nYou have chosen Warrior!\n\nA veteran fighter able to take full bulks of damage.\nYou even dish out a fair amount your self!\n\nHealth: 125\nMaximum Damage: 20\nMinimum Damage: 15\nArmour: 1.25")
    if savedata[0] == "3":
        playerhp = 75
        print("\nYou have chosen Alchemist!\n\nA magical scientist able to make full use of the earthly elements.\nYou poison your oppoments and stall them out with insane healing capabilties!\n\nHealth: 75\nMaximum Damage: 15\nMinimum Damage: 10\nArmour: 0.9")
    savedata[0] = int(savedata[0])
    done = input("\nAre you sure you want this name and class, "+ username+"? (y/n)\n> ").lower()
    if done == "n":
        savedata[0] = 0
        username = ""

SaveData(username, seed, savedata, playerhp)
os.startfile("Main.py")