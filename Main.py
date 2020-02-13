import winsound, time, random
from Save import Save
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

def Lobby():
        global playerclass
        global username
        NewPage()
        location = ""
        print("You are welcomed back into the humbling town.\nThe towns workers are greeting you with wonderful smiles.\n")
        while location != "leave":
            while location not in ["blacksmith","merchant","armourer","help","leave"]:
                location = input("The Blacksmith (\"blacksmith\"), Merchant (\"merchant\") and Armourer (\"armourer\") are here. (type \"leave\" to leave)\n> ").lower()
                if location == "blacksmith":
                        location = ""
                        input("")
                        NewPage()
                if location == "merchant":
                        location = ""
                        input("")
                        NewPage()
                if location == "armourer":
                        location = ""
                        input("")
                        NewPage()
                if location == "help":
                        location = ""
                        input("\nHere you can explore and upgrade your utility within the local town.\n\nThe blacksmith is for upgrading weapons.\nThe store if for buying consumables.\nThe armourer is for Upgrading weapons.\n(enter to continue)\n> ")
                        NewPage()

TitleScreen()
username = ""
while len(username) < 1 or len(username) > 8 or any(ext in username for ext in ["0","1","2","3","4","5","6","7","8","9"," "]):
    username = input("Enter your username: (no numbers or spaces - usernames are not case sensitive)\n> ").capitalize()

seed, savedata, playerhp = Read(username)
#Save(username, seed, savedata, playerhp) #EXAMPLE OF HOW TO SAVE

if savedata[0] == "1":
    playerclass = "Archer"
    winsound.PlaySound("Sounds/arrow.wav", winsound.SND_ASYNC)
if savedata[0] == "2":
    playerclass = "Warrior"
    winsound.PlaySound("Sounds/swords.wav", winsound.SND_ASYNC)
if savedata[0] == "3":
    playerclass = "Alchemist"
    winsound.PlaySound("Sounds/spell.wav", winsound.SND_ASYNC)
print("\nWelcome "+ username+ "... My finest "+ playerclass+ "!\nIf you need a list of commands, type \"help\" at any point.\n")

Lobby()

input("end") #stops program from ending instantly
