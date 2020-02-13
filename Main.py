import winsound, time, random
from Save import SaveData
from Room import Room
from Character import Character, Enemy, Friend
from Item import Item

def Read(username):
    filename = "Save Files/"+ username+ ".txt"
    file = open(filename, "r")
    data = file.readlines()
    file.close()
    seed = data[0]
    seed = seed.replace("\n","")
    seed = seed.replace("[","")
    seed = seed.replace("]","")
    seed = seed.replace(",","")
    seed = seed.replace(" ","")
    list(seed)
    savedata = data[1]
    savedata = savedata.replace("\n","")
    savedata = savedata.replace("[","")
    savedata = savedata.replace("]","")
    savedata = savedata.replace(",","")
    savedata = savedata.replace(" ","")
    list(savedata)
    playerhp = data[2]
    playerhp = playerhp.replace("\n","")
    return seed, savedata, playerhp

def Save():
    global username
    global seed
    global savedata
    global playerhp
    SaveData(username, seed, savedata, playerhp)

def PlayerSound():
    global playerclass
    if playerclass == "Archer":
        winsound.PlaySound("Sounds/arrow.wav", winsound.SND_ASYNC)
    if playerclass == "Warrior":
        winsound.PlaySound("Sounds/swords.wav", winsound.SND_ASYNC)
    if playerclass == "Alchemist":
        winsound.PlaySound("Sounds/spell.wav", winsound.SND_ASYNC)

def NewPage():
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def TitleScreen():
    winsound.PlaySound("Sounds/startup.wav", winsound.SND_ASYNC)
    print("                                              .-'''-.                                ")
    time.sleep(0.05)
    print("                                             '   _    \\                              ")
    time.sleep(0.05)
    print("            _..._                          /   /` '.   \\   _..._  .--.               ")
    time.sleep(0.05)
    print("          .'     '.                  .--./.   |     \\  ' .'     '.|__|               ")
    time.sleep(0.05)
    print("         .   .-.   .    .|          /.''\\\\|   '      |  .   .-.   .--.          .|   ")
    time.sleep(0.05)
    print("    __   |  '   '  |  .' |_    __  | |  | \\    \\     / /|  '   '  |  |        .' |_  ")
    time.sleep(0.05)
    print(" .:--.'. |  |   |  |.'     |.:--.'. \\`-' / `.   ` ..' / |  |   |  |  |    _ .'     | ")
    time.sleep(0.05)
    print("/ |   \\ ||  |   |  '--.  .-/ |   \\ |/(\"'`     '-...-'`  |  |   |  |  |  .' '--.  .-' ")
    time.sleep(0.05)
    print("`\" __ | ||  |   |  |  |  | `\" __ | |\\ '---.             |  |   |  |  | .   | /|  |   ")
    time.sleep(0.05)
    print(" .'.''| ||  |   |  |  |  |  .'.''| | /'\"\"'.\\            |  |   |  |__.'.'| |//|  |   ")
    time.sleep(0.05)
    print("/ /   | ||  |   |  |  |  './ /   | |||     ||           |  |   |  |.'.'.-'  / |  '.' ")
    time.sleep(0.05)
    print("\\ \\._,\\ '|  |   |  |  |   /\\ \\._,\\ '\\'. __//            |  |   |  |.'   \\_.'  |   /  ")
    time.sleep(0.05)
    print(" `--'  `\"'--'   '--'  `'-'  `--'  `\" `'_..._            '--'  ___-'           `'-'   ")
    time.sleep(0.05)
    print("                                    .-'_..._''.            .'/   \\                   ")
    time.sleep(0.05)
    print("                                  .' .'      '.\\   .      / /     \\                  ")
    time.sleep(0.05)
    print("                                 / .'            .'|      | |     |                  ")
    time.sleep(0.05)
    print("             .|      .|         . '            .'  |      | |     |                  ")
    time.sleep(0.05)
    print("    __     .' |_   .' |_    __  | |           <    |      |/`.   .'                  ")
    time.sleep(0.05)
    print(" .:--.'. .'     |.'     |.:--.'.| |            |   | ____  `.|   |                   ")
    time.sleep(0.05)
    print("/ |   \\ '--.  .-'--.  .-/ |   \\ . '            |   | \\ .'   ||___|                   ")
    time.sleep(0.05)
    print("`\" __ | |  |  |    |  | `\" __ | |\\ '.          |   |/  .    |/___/                   ")
    time.sleep(0.05)
    print(" .'.''| |  |  |    |  |  .'.''| | '. `._____.-'|    /\\  \\   .'.--.                   ")
    time.sleep(0.05)
    print("/ /   | |_ |  '.'  |  './ /   | |_  `-.______ /|   |  \\  \\ | |    |                  ")
    time.sleep(0.05)
    print("\\ \\._,\\ '/ |   /   |   /\\ \\._,\\ '/           ` '    \\  \\  \\_\\     /                 ")
    time.sleep(0.05)
    print(" `--'  `\"  `'-'    `'-'  `--'  `\"             '------'  '---`''--'                   ")
    time.sleep(0.05)

def Town():
    global playerclass
    global username
    Save()
    NewPage()
    location = ""
    print("You are welcomed back into the humbling town.\nThe towns workers are greeting you with wonderful smiles.\n")
    while location != "leave":
        while location not in ["blacksmith","merchant","armourer","help","leave"]:
            location = input("The Blacksmith (\"blacksmith\"), Merchant (\"merchant\") and Armourer (\"armourer\") are here. (type \"leave\" to leave)\n> ").lower()
            NewPage()
            if location == "blacksmith":
                    location = ""
                    input("blacksmith\n >")
                    NewPage()
            if location == "merchant":
                    location = ""
                    input("merchant\n >")
                    NewPage()
            if location == "armourer":
                    location = ""
                    input("armourer\n >")
                    NewPage()
            if location == "help":
                    location = ""
                    input("\nHere you can explore and upgrade your utility within the local town.\n\nThe blacksmith is for upgrading weapons.\nThe store if for buying consumables.\nThe armourer is for Upgrading weapons.\n(enter to continue)\n> ")
                    NewPage()
    Menu()

def Menu():
    Save()
    playerinput = ""
    while playerinput not in ["dungeon","town","quit"]:
        NewPage()
        playerinput = input("What would you like to do now my mighty "+ playerclass+ "?\n(A \"dungeon\", back to the \"town\" or \"quit\" the game)\n> ").lower()
    if playerinput == "dungeon":
        playerinput = ""
        Dungeon()
    if playerinput == "town":
        playerinput = ""
        Town()
    if playerinput == "quit":
        playerinput = ""

def Dungeon():
    global username
    global seed
    global savedata
    global playerhp
    global playerclass
    Save()
    NewPage()
    input("dungeon\n> ") #robby put the dungeon code here pls. you may have to global all the stat variables

    Menu()

TitleScreen()
username = ""
while len(username) < 1 or len(username) > 8 or any(ext in username for ext in ["0","1","2","3","4","5","6","7","8","9"," "]):
    username = input("Enter your username: (no numbers or spaces - usernames are not case sensitive)\n> ").capitalize()

seed, savedata, playerhp = Read(username)

if savedata[0] == "1":
    playerclass = "Archer"
    maxhp = 100
    playerhp = 100
    attackmax = 25
    attackmin = 20
    armour = 1
    PlayerSound()
if savedata[0] == "2":
    playerclass = "Warrior"
    maxhp = 125
    playerhp = 125
    attackmax = 20
    attackmin = 15
    armour = 1.25
    PlayerSound()
if savedata[0] == "3":
    playerclass = "Alchemist"
    maxhp = 75
    playerhp = 75
    attackmax = 15
    attackmin = 10
    armour = 0.9
    PlayerSound()

NewPage()
print("\nWelcome "+ username+ "... My finest "+ playerclass+ "!")
playerinput = input("If you need a list of commands, type \"help\" at any point.\n(enter to continue)\n> ").lower()
if playerinput == "help":
    NewPage()
    playerinput = ""
    playerinput = input("You are literally on the welcome screen, "+ username+ "...\nThere is nothing to help you with.\n(enter to continue)\n> ").lower()
    if playerinput == "help":
        NewPage()
        playerinput = ""
        playerinput = input("Ok you can stop now, "+ username+ "...\n(enter to continue)\n> ").lower()
        if playerinput == "help":
            NewPage()
            playerinput = ""
            playerinput = input("Ok, I've had enough of this...\n(enter to continue)\n> ").lower()
            while playerinput == "help":
                NewPage()
                playerinput = ""
                playerinput = input("(enter to continue)\n> ").lower()

Town()