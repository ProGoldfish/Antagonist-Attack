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
        location = ""
        while location not in ["blacksmith","store","armoury","help"]:
                location = input("You are welcomed back into the humbling town, the towns workers are greeting you with wonderful smiles, the Blacksmith(blacksmith), Merchant(store), Armourer(armoury)\n> ").lower()
        if location == "blacksmith":
                input("")
        if location == "store":
                input("")
        if location == "armoruy":
                input("")
        if location == "help":
                input("Here you can explore and upgrade your utility within the local town. The blacksmith is for Upgrading weapons, store if for buying consumables, whilst armoury is for buying new weapons of higher tier") 
                

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
print("Welcome "+ username+ "... My finest "+ playerclass+ "!\nIf you need a list of commands try typing ""Help"" at any point.\n")

Lobby()

input("end") #stops program from ending instantly
