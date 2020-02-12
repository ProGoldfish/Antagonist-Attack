import winsound
from Save import save

def read(username):
	global seed
	global savedata
	global playerhp
	filename = "Save Files/"+ username+ ".txt"
	file = open(filename, "r")
	data = file.readlines()
	file.close()
	seed = data[0]
	seed = seed.replace("\n","")
	savedata = data[1]
	savedata = savedata.replace("\n","")
	playerhp = data[2]
	playerhp = playerhp.replace("\n","")

winsound.PlaySound("Sounds/swords.wav", winsound.SND_ASYNC)

username = ""
while len(username) < 1 or len(username) > 8 or any(ext in username for ext in ["0","1","2","3","4","5","6","7","8","9"," "]):
	username = input("Enter your username: (no numbers or spaces)\n> ").capitalize()

read(username)
save(username, seed, savedata, playerhp)