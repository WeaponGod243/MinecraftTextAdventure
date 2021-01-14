# MAIN
import sys
import time
from sub import tutorial
from sub import saveload
from sub import play
import os
import ctypes
from sub.methods import clear

ctypes.windll.kernel32.SetConsoleTitleW("MCText")


def menutopper(complete, wait):
    MT = open("sub/TextFiles/MenuTopper.txt")
    i = 0
    while i < 8:
        print(MT.readline(), end='')
        if wait:
            time.sleep(0.25)
        i += 1
    print(MT.readline())


def menuselection():
    print("-----------------------------------------------------")
    print("[1]New Game | [2]Load | [3] Tutorial | [4]Quit".center(53))
    while True:
        choices = ["1", "2", "3", "4"]
        num = input("--> ")
        if num in choices:
            choc = int(num)
            return choc
        else:
            print("That was an invalid choice.")


menutopper(1, True)
while True:
    choice = menuselection()
    if choice == 1:
        saveload.save(False, "world")  # not in-world formula save
        clear()
    elif choice == 2:
        play.start(saveload.load())  # in-world formula save
        v = input("Press Enter to go back to menu. (It was just a test load)")
        clear()
    elif choice == 3:
        tutorial.tutorial()
        v = input("Press Enter to go back to menu.")
        clear()
    elif choice == 4:
        print("Thanks for playing! Come back soon!")
        time.sleep(5)
        sys.exit()
    menutopper(1, False)
