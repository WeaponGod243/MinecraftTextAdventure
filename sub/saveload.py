import os
from random import *


def save(inworld, worldname):
    """Saves the world file"""
    if inworld:
        # in-World formula(save world)
        print("In-world")
        filename = worldname.upper() + "-save.txt"
        filepath = "sub/saves/" + filename
        try:
            # File Exists
            trash = open(filepath, "r")
            trash.close()
            f = open(filepath, "w")
            yes = ["Y", "YES"]
            print("Do you wish to overwrite your previous save?")
            yn = input("-->").upper()
            if yn in yes:
                char = "Steve\n"
                location = "89,98,89\n"
                hunger = "50\n"
                health = "50\n"
                file = [char, location, hunger, health]
                f.writelines(file)
                print("World has been saved")
            else:
                print("Cancelling save")
            input("Press Enter to continue...")
        except FileNotFoundError:
            # File does not exist
            f = open(filepath, "w+")
            char = "Steve\n"
            location = "89,98,89\n"
            hunger = "50\n"
            health = "50\n"
            file = [char, location, hunger, health]
            f.writelines(file)
            print("World has been saved")
            input("Press Enter to continue...")
    else:
        # Not in-World formula(create world)
        print("Not In-world")
        print("What name do you want for this world?")
        chosenname = input("-->").upper()
        filename = chosenname + "-save.txt"
        filepath = "sub/saves/" + filename
        try:
            # File Exists
            trash = open(filepath, "r")
            trash.close()
            f = open(filepath, "w")
            yes = ["Y", "YES"]
            print("Do you wish to overwrite your previous save named " + chosenname + "?")
            yn = input("-->").upper()
            if yn in yes:
                while True:
                    print("Input the character name for this world")
                    char = input("-->")
                    if char.isalnum():
                        char = char + "\n"
                        break
                    print("That was not a proper input.")
                x = str(randint(-2048, 2048))
                y = str(randint(120, 150))
                z = str(randint(-2048, 2048))
                location = x + "," + y + "," + z + "\n"
                hunger = "100\n"
                health = "100\n"
                file = [char, location, hunger, health]
                f.writelines(file)
                print("World has been overwritten")
            else:
                print("Cancelling Creation")
            input("Press Enter to continue...")
        except FileNotFoundError:
            # File does not exist
            f = open(filepath, "w+")
            while True:
                print("Input the character name for this world")
                char = input("-->")
                if char.isalnum():
                    char = char + "\n"
                    break
                print("That was not a proper input.")
            x = str(randint(-2048, 2048))
            y = str(randint(120, 150))
            z = str(randint(-2048, 2048))
            location = x + "," + y + "," + z + "\n"
            hunger = "100\n"
            health = "100\n"
            file = [char, location, hunger, health]
            f.writelines(file)
            print("World has been created")
            input("Press Enter to continue...")


def load():
    """Loads the world file"""
    # TODO create load function
    print("load")
    sd = "sub/saves"
    flist = os.listdir(sd)
    wlist = []
    for i in flist:
        index = i.find("-")
        wname = i[0:index]
        wlist.append(wname)

    print("Which save would you like to load?")
    print("--------------------")
    j = 1
    for n in wlist:
        print("[%d]%s" % (j, n))
        j += 1
    while True:
        try:
            decide = input("-->")
            if decide.isnumeric():
                worldname = wlist[int(decide)-1]
                break
            else:
                print("Incorrect input")
        except IndexError:
            print("That number is too high for the selection. Try again.")

    return worldname
