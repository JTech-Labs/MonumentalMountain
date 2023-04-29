import sys,time,random,os
# This is MonumentalMountain Aplpha v0.0.1
# This "Alpha Game Programm" (CC-BY-NO) was created by "Javier Fuentes-Hermoso"
# MonumentalMountain is licenced under the GNU GPLv3 licence by GAMAX-INTERACTIVE, part of the JAI-INNOVATIONS
def stop_all():
    print(f"Input invalid, sorry {name}, you lose...")
    quit()

inventory = str(0)
health = int(100)
protection = int(0)
power = int(1)
magic = int(0)

while True:
    if input() == ';':
        print(f"\n {inventory} \n {health} \n {protection} \n {power} \n {magic} \n")
        continue


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

print_slow("Welcome to MonumentalMountain Alpha v0.0.1. Created by GAMAX-INTERACTIVE")
print('\n')

print_slow("Legends have been told about the Mysterious Monumental Mountain, a realm accessible only while in a certain mental state that must be reached through sleep.")
print('\n')

print_slow("A place created at the dawn of humankind by the Supreme Planetary Council of Intelligence to test humankind until they are advanced enough as a species to join the Supreme Council")
print('\n')

print_slow("You, a simple human who have only read about this mysterious realm in medieval history books, go to bed in peace without the knowledge that at exactly midnight of the summer equinox of 2023 eveyone on the dark and light side of the Earth unconciously decides to sleep all at the same time.")
print('\n')

print_slow("Only the human that is most conciously unprepared but subconciously ready would be chosen to go and stand for their species. ")

print_slow("And that one specific person,  at this one specific time happens to be...")
print('\n')
print_slow("You")

print('\n')
print('\n')
print('\n')

print("Welcome to the Monumental Mountain. We will lead you through the terrain, but you must make the vital decisions as you progress")

print("Please type in all lowercase")

    yesno1 = input("Are you ready?: ")

if yesno1 == "yes":
    print_slow("Starting . . . . . . . . . . . . . . . .")
else:
    quit()


os.system('cls' if os.name == 'nt' else "printf '\033c'")

print_slow("You're lost and scared, you've lost control. You are trapped in a nightmare where you can't stop falling. Incomprehensible lights, colours and emotions fly past you at impossible speeds while reality and imagination merge into a flash of white that overwhelms you as you collide with the ground.")

print('\n')

print_slow("You don't remember anything, not even your name or age. All you know is that you are at the edge of a crossroads and that something is forcing you to move forewards")
print('\n')
name = input("After some consideration, you decide to refer to yourself as:   ")

print('\n')
print('\n')

print_slow("You look forewards, at the crossroads. A path directly ahead of you leads to a giant grey,  snow-capped mountain shrouded by cloud which half hides the bright sun. ")
print_slow("To the left there is a path leading to a green and life-filled forest. The treetops are shrouded by storm clouds and a dark atmosphere emanates from it. ")
print_slow("The left path leads to a barren and arid desert with a few littered canyons and scorching heat that can be felt from here.")

print('\n')
dir1 = input("You decide to go:   ")

if dir1 == "left":
    print_slow("Even though you might not find water there you think it is the best option for refuge.")
    while True:
            print_slow("Even though you might not find water there you think it is the best option for refuge.")
            time.sleep(5)
            
            print_slow("You slowly stroll forewards, brushing the sand with your feet as the sun scorches the back of your neck.")
            print("\n")
            
            print_slow("You see a set of large rocks that looks like could be good for refuge and might be a bit humid. You can also see a small shadow far away and think it could be an oasis. Or you could carry on just incase you find anything better.")
            print('\n')
            
            dir2 = input("You chose to go")
            if dir2 =='shadow':
                print_slow("")
            
            elif dir2 == 'rocks':
                print_slow("")
            
            elif dir2 == 'forewards':
                print_slow("")
elif dir1 == "forewards":
    print_slow("You are filled with a burning curiosity and decide to make headway for the mountain.")
elif dir1 == "right":
    print_slow("You decide that this is the best option for food and that you will be able to survive easily there.")
else:
    print(f"Input invalid, sorry {name}, you lose...")
    quit()
