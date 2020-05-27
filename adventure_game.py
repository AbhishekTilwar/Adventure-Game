import time
import random


def start_game():
    Object = []
    Animals = random.choice(["Lion", "Tiger", "Dragon"])
    starting_Intro(Object, Animals)
    Forest(Object, Animals)


def starting_Intro(Object, Animals):
    print_line("\t Welcome to Your Dream Adventure!")
    print_line("\n\n \t\t *In your Dreams*\n")
    print_line("Lets Go..!\n")
    print_line("So,Imagine You are standing in an dark night sky in forest.\n")
    print_line("You think a " + Animals + " is somewhere around here.\n")
    print_line("In front of you is a big thing coming....")
    print_line("You don't know what is it\n")
    print_line("you hear sound to you left there is a noise of Animal.\n")
    print_line("You find stick & you hold stick in hand, as dagger alert.\n")


def Forest(Object, Animals):
    print_line("Enter 'Tree': to hide behind the trees...!")
    print_line("Enter 'Hut': to hide in hut behind ...!")
    print_line("What would you like to do?\n")
    while True:
        Option = input("(Please enter what would you do...)\n")
        if Option == "Tree":
            Trees(Object, Animals)
            break
        elif Option == "Hut":
            Hut(Object, Animals)
            break


def Trees(Object, Animals):
    print_line("\nYou walk towards the right.")
    print_line("\nYou are about to hide behind the tree\n")
    print_line("At the same time there steps out a " + Animals + ".")
    print_line("\nYou find this is the " + Animals)
    print_line("\nThe " + Animals + " attacks you!\n")
    if "stick" not in Object:
        print_line("You feel bit under-prepared for this, Get terrified...\n")
    while True:
        choice2 = input("Would you like to (Fight) fight or (Run) "
                        "run away?")
        if choice2 == "Fight":
            if "sword" in Object:
                print_line("\nAs the " + Animals + " moves to attack,")
                print_line(" you unsheath a sword.")
                print_line("\nThe Sword shines brightly in ")
                print_line("\nBut the " + Animals + " look at your shiny")
                print_line("and runs away!")
                print_line("\nYou got rid of the " + Animals + " You Won..!\n")
            else:
                print_line("\nYou do your best...")
                print_line("but your dagger is no match for the " + Animals)
                print_line("\nYou have been defeated!\n")
            Replay()
            break
        if choice2 == "Run":
            print_line("\nYou run back into the main highway")
            print_line("\nLuckily, you don't seem to have been followed.\n")
            print_line("\nYou are now free..!")
            forest(Object, Animals)
            break


def Hut(Object, Animals):
    if "stick" in Object:
        print_line("\nYou frigthened .")
        print_line("\nYou've started running backward...you are terrified")
        print_line("\nYou find a Small hut .\n")
    else:
        print_line("\nYou run towards Hut...")
        print_line("\nIt turns out to be only a very old and damage hut....")
        print_line("\nYour eye catches a shining of metal behind a box.")
        print_line("\nYou have found the Shining Sword !")
        print_line("\nYou get towards your dagger")
        print_line("taking the sword with you.")
        print_line("\nYou walk back out to the forest....You are Safe...!\n")
        Object.append("stick")
    Replay()


def Replay():
    again = input("Do you want to play Game again? (Y/N)")
    if again == "Y":
        print_line("\n\n\n Great! Restarting the game ...\n\n\n")
        Replay()
    elif again == "N":
        print_line("\nThanks for playing! See you next time...!\n")
    else:
        Replay()


def print_line(msg):
    print(msg)
    time.sleep(1.5)

start_game()
