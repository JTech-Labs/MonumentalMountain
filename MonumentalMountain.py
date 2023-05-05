import sys, time, random, os
# This is MonumentalMountain Alpha v0.0.2
# This "Alpha Game Program" (CC-BY-NO) was created by "Javier Fuentes-Hermoso"
# MonumentalMountain is licensed under the GNU GPLv3 license by GAMAX-INTERACTIVE, part of the JAI-INNOVATIONS
inventory = str("_")
health = int(100)
protection = int(0)
power = int(1)
magic = int(0)
sh1 = int(0)
def playerstatus():
    print('\n')
    print(f"\n Inventory: {inventory} \n Health: {health} \n Protection: {protection} \n Power: {power} \n Magic: {magic} \n")
    print('\n')

def stop_all():
    print(f"Input invalid, sorry {name}, you lose...")
    time.sleep(5)
    quit()

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

print_slow("Welcome to MonumentalMountain Alpha v0.0.2 Created by GAMAX-INTERACTIVE")
print('\n')

print_slow("Legends have been told about the Mysterious Monumental Mountain, a realm accessible only while in a certain mental state that must be reached through sleep.")
print('\n')

print_slow("A place created at the dawn of humankind by the Supreme Planetary Council of Intelligence to test humankind until they are advanced enough as a species to join the Supreme Council")
print('\n')

print_slow("You, a simple human who have only read about this mysterious realm in medieval history books, go to bed in peace without the knowledge that at exactly midnight of the summer equinox of 2023 everyone on the dark and light side of the Earth unconsciously decides to sleep all at the same time.")
print('\n')

print_slow("Only the human that is most consciously unprepared but subconsciously ready would be chosen to go and stand for their species. ")

print_slow("And that one specific person,  at this one specific time happens to be...")
print('\n')
print_slow("You")

print('\n')
print('\n')
print('\n')

print("Welcome to the Monumental Mountain. We will lead you through the terrain, but you must make the vital decisions as you progress")

print("Please type in all lowercase, you will know what to type because it is marked with two asterisk.")

yesno1 = input("Are you ready, *yes* or no*?: ")

if yesno1 == "yes":
    print_slow("Starting . . . . . . . . . . . . . . . .")
else:
    quit()


os.system('cls' if os.name == 'nt' else "printf '\033c'")

print_slow("You're lost and scared, out of control. You are trapped in a nightmare where you can't stop falling. Incomprehensible lights, colors and emotions fly past you at impossible speeds while reality and imagination merge into a flash of white that overwhelms you as you collide with the ground.")

print('\n')

print_slow("You don't remember anything, not even your name or age. All you know is that you are at the edge of a crossroads and that something is forcing you to move forwards")
print('\n')
name = input("After some consideration, you decide to refer to yourself as:   ")

print('\n')
print_slow("The first thing you do is notice a cuff bracelet made from gold and copper with incrusted diamonds that contains a lot of weird engraved text in some kind of foreign language not known to man and something in English, it says:")
playerstatus()
print_slow("You discover that it cannot be taken off and decide not to worry about it too much and focus on what is directly in front of you.")
print('\n')
print('\n')

print_slow("You look *forwards*, at the crossroads. A path directly ahead of you leads to a giant grey, snow-capped mountain shrouded by clouds which half hides the bright sun. ")
print_slow("To the *right* there is a path leading to a green and life-filled forest. The treetops are shrouded by storm clouds and a dark atmosphere emanates from it. ")
print_slow("The *left* path leads to a barren and arid desert with a few littered canyons and scorching heat that can be felt even from here.")

print('\n')
dir1 = input("You decide to go:   ")

if dir1 == "left":
    print_slow("Even though you might not find water there you think it is the best option for refuge. ")
    while True:
        print_slow("You slowly stroll forwards, brushing the sand with your feet as the sun scorches the back of your neck.")
        print("\n")
        
        print_slow("You see a set of large *rocks* that look like could be good for refuge and might be a bit humid. You can also see a small *shadow* far away and think it could be an oasis. Or you could carry on *forwards* just incase you find anything better.") # You can as well always go back (not yet implemented).
        print('\n')
        
        dir2 = input("You chose to go:  ")
        if dir2 =='shadow':
            if sh1 == 1:
                print_slow("After some walking, you find a palm tree with an \"X\" carved into it, as this had always meant treasure in your world, you dig a few centimeters and find a small coin, after you touch it, you cuff bracelet updates, it reads:")
                inventory = inventory + ("compass_")
                health = health + 50
                protection = protection + 5
                power = power + 3
                playerstatus()
                sh1 = sh1 + 1
                print_slow("You figure the number after the object must be its level. After examining your cuff again, you decide to carry on.")
            else:
                print_slow("You see the tree with the \"X\" on it and the hole. There is nothing more to see here.")
        
        elif dir2 == 'rocks':
            print_slow("You go to the rocks to see what there is. You find a steep and narrow staircase that leads downwards")
        
        elif dir2 == 'forwards':
            print_slow("You decide to go forwards as you are not really interested in what you can see from here. As you try and block the sun with your hand, you trip over a small rock, falling down a canyon.")
            print_slow("Surprisingly, you survive. But  only to be met with a giant cockroach.")
            fight1 = input("Do you want to *fight* or would you rather *run*?:  ")
            if fight1 == "run":
                print("you instantly run, you find that there is a less steep hill nearby that can help you get back to the start of the dessert.")
            elif fight1 == "fight":
                if [power >= 7] or [protection >= 7]:
                    print("")
                else:
                    print("Before you even start to fight, you get a heart attack as you where not ready, you die. X( ")
                    time.sleep(5)
                    quit()
            

        else:
            stop_all()

elif dir1 == "forwards":
    print_slow("You are filled with a burning curiosity and decide to make headway for the mountain.")

elif dir1 == "right":
    print_slow("You decide that this is the best option for food and that you will be able to survive easily there.")

else:
    stop_all()
