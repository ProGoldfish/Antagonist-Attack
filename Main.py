import winsound
from Save import Save

def Read(username):
	global seed
	global savedata
	global playerhp
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

username = ""
while len(username) < 1 or len(username) > 8 or any(ext in username for ext in ["0","1","2","3","4","5","6","7","8","9"," "]):
	username = input("Enter your username: (no numbers or spaces - usernames are not case sensitive)\n> ").capitalize()

Read(username)
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

print("Welcome "+ username+ "... My finest "+ playerclass+ "!")

input("end") #stops program from ending instantly