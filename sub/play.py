import time

from sub.methods import clear
from sub.methods import loadingtiles


def load(worldname):
    global char
    global location
    global hunger
    global health
    global x
    global y
    global z
    print("Loading", end='\n')
    print(loadingtiles("World data", 11, 0), end='\r')
    time.sleep(0.3)
    filename = worldname + "-save.txt"
    print(loadingtiles("World data", 11, 1), end='\r')
    time.sleep(0.3)
    filepath = "sub/saves/" + filename
    print(loadingtiles("World data", 11, 2), end='\r')
    time.sleep(0.3)
    world = open(filepath, "r+")
    print(loadingtiles("World data", 11, 3), end='\r')
    time.sleep(0.3)
    char = world.readline().strip("\n")
    print(loadingtiles("World data", 11, 4), end='\r')
    time.sleep(0.3)
    location = world.readline().strip("\n")
    print(loadingtiles("World data", 11, 5), end='\r')
    time.sleep(0.3)
    hunger = world.readline().strip("\n")
    print(loadingtiles("World data", 11, 6), end='\r')
    time.sleep(0.3)
    health = world.readline().strip("\n")
    print(loadingtiles("World data", 11, 7), end='\r')
    time.sleep(0.3)
    coords = location.split(',')
    print(loadingtiles("World data", 11, 8), end='\r')
    time.sleep(0.3)
    x = coords[0]
    print(loadingtiles("World data", 11, 9), end='\r')
    time.sleep(0.3)
    y = coords[1]
    print(loadingtiles("World data", 11, 10), end='\r')
    time.sleep(0.3)
    z = coords[2]
    print(loadingtiles("World data", 11, 11), end='\r')
    time.sleep(0.3)
    clear()
    print("Loaded.", end="\r")
    time.sleep(0.7)
    print("Loaded..", end="\r")
    time.sleep(0.7)
    print("Loaded...", end="\r")
    time.sleep(0.7)


def stats():
    print("=======================================================")
    chara = char.ljust(8)
    hxh = "HP " + health + "/Hunger " + hunger
    hxh = hxh.ljust(16)
    locat = location.ljust(14)
    stats_heading = chara + "   " + hxh + "  Location: " + locat + "\n"
    print(stats_heading)


def choices():
    print("[1]Look")
    print("[2]Move")
    print("[3]Mine")
    print("[4]Waypoint")
    print("[5]Build/Upgrade")
    print("[6]Inventory")
    print("[7]Travel")
    while True:
        choice = input("-->")
        if choice.isnumeric():
            choice = int(choice)
            if choice <= 7:
                break
            else:
                print("Choice too high.")
        else:
            print("Invalid choice.")

    return choice


def gameplay():
    clear()
    stats()
    print("You wake up in your world. What will you do?")
    choc = 8
    if choc == 1:
        print("choice1")
    elif choc == 2:
        print("choice2")
    elif choc == 3:
        print("choice3")
    elif choc == 4:
        print("choice4")
    elif choc == 5:
        print("choice5")
    elif choc == 6:
        print("choice6")
    elif choc == 7:
        print("choice7")
    else:
        clear()
        print("I don't know how in the world you're seeing this because of the precautions put into place, "
              "so you have seriously hit a bad error. I'm going to have to crash your game now, sorry.")
        print("Crashing in 10", end='\r')
        time.sleep(1)
        print("Crashing in 9", end='\r')
        time.sleep(1)
        print("Crashing in 8", end='\r')
        time.sleep(1)
        print("Crashing in 7", end='\r')
        time.sleep(1)
        print("Crashing in 6", end='\r')
        time.sleep(1)
        print("Crashing in 5", end='\r')
        time.sleep(1)
        print("Crashing in 4", end='\r')
        time.sleep(1)
        print("Crashing in 3", end='\r')
        time.sleep(1)
        print("Crashing in 2", end='\r')
        time.sleep(1)
        print("Crashing in 1", end='\r')
        time.sleep(1)
        print("Crashing in 0", end='\r')
        time.sleep(1)
        raise Exception("Sorry you had a bad time. Contact the developer if you get this error xP")


def start(worldname):
    load(worldname)
    gameplay()
