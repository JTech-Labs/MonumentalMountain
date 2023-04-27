import sys,time,random,os
# This is MonumentalMountain Aplpha v0.0.1
# This "Alpha Game Programm" (CC-BY-NO) was created by "Javier Fuentes-Hermoso"
# MonumentalMountain is licenced under the GNU GPLv3 licence by GAMAX-INTERACTIVE, part of the JAI-INNOVATIONS
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

print_slow("Welcome to MonumentalMountain Alpha v0.0.1. Created by GAMAX-INTERACTIVE")
print('\n')

print_slow("Legends have been told about the Mysterious Monumental Mountain, a realm only accessible though sleep in very specific circumstances.")
print('\n')

print_slow("A place made at the begining of humanity by the supreme planetary council of intelligence to test humankind until they are balanced enough as a species to join the council")
print('\n')

print_slow("You, a simple human who have only read about these things in medieval library books, go to bed in peace without the knowledge that exactly at midnight of the summer equinox of 2023 eveyone on the dark and light side of the Earth unconciously decide to sleep all at the same time.")
print('\n')

print_slow("Only the human that is most conciously unprepared by subconciously ready that would be chosen to go and stand for their species.")

print_slow("And that one specific person, this one specific time happens to be...")
print_slow("You")

print('\n')
print('\n')
print('\n')

print("Welcome to the Monumental Mountain. We will lead you through the terrain and youu have to make decisions as you go along and please ansewer in all lowercase.")

yesno1 = input("Are you ready?: ")

if yesno1 == "yes":
    print_slow("Starting . . . . . . . . . . . . . . . .")
else:
    quit()


os.system('cls' if os.name == 'nt' else "printf '\033c'")

print_slow("You're lost scared, without control. Like being trapped in a nightmare where you can't stop falling. Lights colours and feelings that you wouldn't even be able to imagine fly past you at imposible speeds while reality and imagination merge into a flush of white that blanks everything out as you hit the floor.")

print('\n')

print_slow("You don't remember anything, not even your name or age. All you know is that you are at the edge of a crossroads and that something is forcing you forewards")
print('\n')
name = input("After some thinking you decide to refer to yourself as:   ")

print('\n')
print('\n')

print_slow("You look forewards to the  crossroads. A path directly infront of you leads to a giant mountain in a field that is half hiding a bright sun. ")
print_slow("To the left there is a path leading to a live looking forrest under stormy clouds and with a dark atmosphere to it. ")
print_slow("The left path leads to a wide dessert with a few cannyons and a heat that can be felt from here.")

print('\n')
dir1 = input("You decide to go:   ")

if dir1 == "left":
    print_slow("Even though you might not find water there you think it is the best option for refuge.")
elif dir1 == "forewards":
    print_slow("You think that this is the safest option and that you are sure to find everything you need there.")
elif dir1 == "right":
    print_slow("You decide that this is the best option for food and that you will be able to survive easily there.")
else:
    print(f"Input invalid, sorry {name}, you lose...")
    quit()
