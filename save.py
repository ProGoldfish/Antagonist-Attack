def save(username,seed,savedata,maxhp,playerhp,attackmax,attackmin,armour):
    filename = "Save Files/"+ username + ".py"
    file = open(filename, "w")
    data = ["seed = "+ str(seed), "\n", "savedata = "+ str(savedata), "\n", "maxhp = "+ str(maxhp), "\n", "playerhp = "+ str(playerhp), "\n", "attackmax = "+ str(attackmax), "\n", "attackmin = "+ str(attackmin), "\n", "armour = "+ str(armour)]
    for i in range(len(data)):
        file.writelines(str(data[i]))
    file.close()