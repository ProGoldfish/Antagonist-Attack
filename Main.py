import winsound
from Save import save

username = ""
while len(username) < 1 or len(username) > 8 or any(ext in username for ext in ["0","1","2","3","4","5","6","7","8","9"," "]):
	username = input("Enter your username: (no numbers or spaces)\n> ").capitalize()
filename = username
print(filename)
input(__import__(filename))
input(seed)
