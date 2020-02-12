import os
account = ""
while account not in ["y","n"]:
	account = input("Do you already have an account? (y/n)\n> ").lower()
if account == "y":
	os.startfile("Main.py")
if account == "n":
	os.startfile("Character Creation.py")