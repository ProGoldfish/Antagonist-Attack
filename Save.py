def save(username,seed,savedata,playerhp):
    filename = "Save Files/"+ username + ".txt"
    file = open(filename, "w")
    data = [str(seed), "\n", str(savedata), "\n", str(playerhp)]
    for i in range(len(data)):
        file.writelines(str(data[i]))
    file.close()
