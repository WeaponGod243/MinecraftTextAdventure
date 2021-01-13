# MAIN
import sys
import time
from sub import tutorial


def menutopper(complete):
    MT = open("sub/TextFiles/MenuTopper.txt")
    i = 0
    while i < 8:
        print(MT.readline(), end='')
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


menutopper(1)
while True:
    choice = menuselection()
    if choice == 1:
        break
    elif choice == 2:
        break
    elif choice == 3:
        tutorial.tutorial()
    elif choice == 4:
        print("Thanks for playing! Come back soon!")
        sys.exit()
