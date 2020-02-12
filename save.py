def save(username,seed,savedata,maxhp,playerhp,attackmax,attackmin,armour):
    filename = username + ".py"
    file = open(filename, "w")
    data = ["seed = "+ str(seed), "\n", "savedata = "+ str(savedata), "\n", "playerhp = "+ str(playerhp)]
    for i in range(len(data)):
        file.writelines(str(data[i]))
    file.close()