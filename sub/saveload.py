import os


def save(inworld, worldname):
    """Saves the world file"""
    if inworld:
        # in-World formula(save world)
        print("In-world")
        filename = worldname + "-save.txt"
        filepath = "sub/saves/" + filename
        try:
            # File Exists
            trash = open(filepath, "r")
            trash.close()
            f = open(filepath, "w")
            yes = ["Y", "YES"]
            yn = input("Do you wish to overwrite your previous save?: ").upper()
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
    else:
        # Not in-World formula(create world)
        print("Not In-world")
        chosenname = input("What name do you want for this world?: ")
        filename = chosenname + "-save.txt"
        filepath = "sub/saves/" + filename
        try:
            # File Exists
            trash = open(filepath, "r")
            trash.close()
            f = open(filepath, "w")
            yes = ["Y", "YES"]
            yn = input("Do you wish to overwrite your previous save named " + chosenname + "?: ").upper()
            if yn in yes:
                char = "Steve\n"
                location = "0,0,0\n"
                hunger = "100\n"
                health = "100\n"
                file = [char, location, hunger, health]
                f.writelines(file)
                print("World has been overwritten")
            else:
                print("Cancelling Creation")
        except FileNotFoundError:
            # File does not exist
            f = open(filepath, "w+")
            char = "Steve\n"
            location = "0,0,0\n"
            hunger = "100\n"
            health = "100\n"
            file = [char, location, hunger, health]
            f.writelines(file)
            print("World has been created")


def load():
    # TODO create load function
    print("load")
