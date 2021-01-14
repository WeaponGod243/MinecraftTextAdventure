import time

from sub.methods import clear
from sub.methods import loadingtiles


def start(worldname):
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
    char = world.readline()
    print(loadingtiles("World data", 11, 4), end='\r')
    time.sleep(0.3)
    location = world.readline()
    print(loadingtiles("World data", 11, 5), end='\r')
    time.sleep(0.3)
    hunger = world.readline()
    print(loadingtiles("World data", 11, 6), end='\r')
    time.sleep(0.3)
    health = world.readline()
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
    time.sleep(0.3)
    print("Loaded..", end="\r")
    time.sleep(0.3)
    print("Loaded...", end="\r")
    time.sleep(0.3)
