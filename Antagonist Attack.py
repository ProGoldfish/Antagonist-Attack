import random, winsound, os
from save import save
seed = []
savedata = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
username = ""

#winsound.Beep(1000, 100) #plays a beep. 1st arguement is hz and second is ms
#winsound.PlaySound("Sounds/test.wav", winsound.SND_FILENAME) #waits until the sound has finished playing to continue
winsound.PlaySound("Sounds/test2.wav", winsound.SND_ASYNC) #continues the program while the sound is playing

for i in range(200):
    seed.append(random.randint(0,9))

done = "n"
while done == "n":
    while len(username) < 1 or len(username) > 8 or any(ext in username for ext in ["0","1","2","3","4","5","6","7","8","9"," "]):
        username = input("Please enter a username that you will remember: (no numbers or spaces)\n> ").capitalize()

    while savedata[0] not in ["1","2","3"]:
        savedata[0] = input("\nChoose a class:\nArcher (1)\nWarrior (2)\nAlchemist (3)\n> ")

    if savedata[0] == "1":
        maxhp = 100
        playerhp = 100
        attackmax = 25
        attackmin = 20
        armour = 1
        print("\nYou have chosen Archer!\n\nA ranger able to make full use of the long range weapons.\nYou shoot down your enemies but be careful not to get hit!\n\nHealth: {}\nMaximum Damage: {}\nMinimum Damage: {}\nArmour: {}".format(maxhp, attackmax, attackmin, armour)) 
    if savedata[0] == "2":
        maxhp = 125
        playerhp = 125
        attackmax = 25
        attackmin = 20
        armour = 1.25
        print("\nYou have chosen Warrior!\n\nA veteran fighter able to take full bulks of damage.\nYou even dish out a fair amount your self!\n\nHealth: {}\nMaximum Damage: {}\nMinimum Damage: {}\nArmour: {}".format(maxhp, attackmax, attackmin, armour))
    if savedata[0] == "3":
        maxhp = 75
        playerhp = 75
        attackmax = 15
        attackmin = 10
        armour = 0.9
        print("\nYou have chosen Alchemist!\n\nA magical scientist able to make full use of the earthly elements.\nYou poison your oppoments and stall them out with insane healing capabilties!\n\nHealth: {}\nMaximum Damage: {}\nMinimum Damage: {}\nArmour: {}".format(maxhp, attackmax, attackmin, armour))

    savedata[0] = int(savedata[0])
    done = input("\nAre you sure you want this name and class, "+ username+"? (y/n)\n> ").lower()
    if done == "n":
        savedata[0] = 0
        username = ""

save(username,seed,savedata,maxhp,playerhp,attackmax,attackmin,armour)

os.startfile("Main.py")