import os


def clear():
    os.system('cls')
    print("")


def loadingtiles(data, mx, i):
    dots = ""
    tiles = ""
    d = mx - i
    for j in range(0, d):
        dots = dots + "."
    for t in range(0, i):
        tiles = tiles + "█"
    string = data + " " + str(i) + "/" + str(mx) + "[" + tiles + dots + "]"
    return string
