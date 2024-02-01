import time,os,sys

def clear():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

def printSlow(stri):
    for letter in stri:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

clear()

name = ""

#Intro
def intro():
    printSlow("Welcome to MonumentalMountain Alpha v0.0.2r Created by GAMAX-INTERACTIVE")
    print('\n')

    printSlow("Legends have been told about the Mysterious Monumental Mountain,\
a realm accessible only while in a certain mental state that must be reached through sleep.")
    print('\n')

    printSlow("A place created at the dawn of humankind by the Supreme Planetary Council of Intelligence \
to test humankind until they are advanced enough as a species to join the Supreme Council")
    print('\n')

    printSlow("You, a simple human who have only read about this mysterious realm in medieval history books, \
go to bed in peace without the knowledge that at exactly midnight of the summer equinox of 2023 \
everyone on the dark and light side of the Earth unconsciously decides to sleep all at the same time.")
    print('\n')

    printSlow("Only the human that is most consciously unprepared but subconsciously \
ready would be chosen to go and stand for their species. ")

    printSlow("And that one specific person,  at this one specific time happens to be...")
    print('\n')
    print('\n')
    printSlow("You")
    time.sleep(2)
    print('\n')
    clear()
    print('\n')
    print('\n')

    print("Welcome to the Monumental Mountain. We will lead you through\
the terrain, but you must make the vital decisions as you progress. If you ever need help, type in \"Help\"\n\n\
!!WARNING!!, THIS GAME IS INPIRED BY COLOSSAL CAVE ADVENTURE, YOUR PROGRESS WILL NOT BE SAVED!, \
YOU HAVE BEEN WARNED!")

    print("The available prompts will be directions (e.g. forewards, back, right, left) and several more,\
 if you need help, just type in \"Help\".\n")

    yesno1 = input("Are you ready, *yes* or *no*?: ").title()

    if yesno1 == "Yes":
        printSlow("Starting . . . . . . . . . . . . . . . .")

        clear()
    else:
        printSlow("You have decided that you are not yet ready for this. The council will chose someone\
    =else to replace you. Remember though, you can always come back when you are ready...")
        quit()


    printSlow("You're lost and scared, out of control. You are trapped in a nightmare where you can't stop falling.\
 Incomprehensible lights, colors and emotions fly past you at impossible speeds while reality and\
 imagination merge into a flash of white that overwhelms you as you collide with the ground.")

    print('\n')

    printSlow("You don't remember anything, not even your name or age. All you know is that you are at the edge of\
 a crossroads and that something is forcing you to move forwards")
    print('\n')
    name = input("After some consideration, you decide to refer to yourself as:   ")

    print('\n')
    printSlow(f"Now {name}, the first thing you do is notice a cuff bracelet made from gold and copper with incrusted\
 gems that contains a lot of weird engraved text in some kind of foreign language not known to to your kind.\n")
    # PlayerStatus()
    printSlow("You discover that it cannot be taken off and decide not to worry about it too much and focus on\
 what is directly in front of you.")
    print('\n')
    print('\n')
    return name