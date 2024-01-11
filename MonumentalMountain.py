import sys, time, random, os, webbrowser
from modules import PlayerStatus, stop_all, print_slow, sh1, fight1_2
from intro import intro
# This is MonumentalMountain Alpha v0.0.2
# This "Alpha Game Program" (CC-BY-NO) was created by "Javier Fuentes-Hermoso"
# MonumentalMountain is licensed under the GNU GPLv3 license by GAMAX-INTERACTIVE, part of the JAI-INNOVATIONS

    #Main game
playgame = input("Do you want the introduction [y,n]?:  ")
if playgame == "y" or playgame == "Y":
    intro()
elif playgame == "n" or playgame == "N":
    print('\n')


print('\n')
print('\n')

print("Welcome to the Monumental Mountain. We will lead you through the terrain, but you must make the vital decisions as you progress")

print("Please type in all lowercase, you will know what to type because it is marked with two asterisk.")

yesno1 = input("Are you ready, *yes* or *no*?: ")

if yesno1 == "yes":
    print_slow("Starting . . . . . . . . . . . . . . . .")
    TimeSleep = float(0.5)
else:
    print_slow("You have decided that you are not yet ready for this. The council will chose someone else to replace you. Remember though, you can always come back when you are ready...")
    quit()


print_slow("You're lost and scared, out of control. You are trapped in a nightmare where you can't stop falling. Incomprehensible lights, colors and emotions fly past you at impossible speeds while reality and imagination merge into a flash of white that overwhelms you as you collide with the ground.")

print('\n')

print_slow("You don't remember anything, not even your name or age. All you know is that you are at the edge of a crossroads and that something is forcing you to move forwards")
print('\n')
name = input("After some consideration, you decide to refer to yourself as:   ")

print('\n')
print_slow("Now {name}, he first thing you do is notice a cuff bracelet made from gold and copper with incrusted diamonds that contains a lot of weird engraved text in some kind of foreign language not known to man and something in English, it says:")
PlayerStatus()
print_slow("You discover that it cannot be taken off and decide not to worry about it too much and focus on what is directly in front of you.")
print('\n')
print('\n')

print_slow("You look *forwards*, at the crossroads, a slightly superliminal place. A path directly ahead of you leads to a giant grey, snow-capped mountain shrouded by clouds which half hides the bright sun. ")
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
                PlayerStatus()
                sh1 = sh1 + 1
                print_slow("You figure the number after the object must be its level. After examining your cuff again, you decide to carry on.")
            else:
                print_slow("You see the tree with the \"X\" on it and the hole. There is nothing more to see here.")
        
        elif dir2 == 'rocks':
            print_slow("You go to the rocks to see what there is. You find a steep and narrow staircase that leads downwards.")
            if str("_Light-Necklace_") in Inventory:
                print_slow("Just before you go down the stairs, you find a small crack in the wall of one of the rocks that matches the shape of your necklace.")
                print_slow("You decide to place the necklace in. Suddenly, a flash of light engulfs you and you feel as if you where thrown at the speed of light forwards and you don't have any way of stopping it.")
                print_slow("\nIt all goes white.")
                webbrowser.open('')
        elif dir2 == 'forwards':
            print_slow("You decide to go forwards as you are not really interested in what you can see from here. As you try and block the sun with your hand, you trip over a small rock, falling down a canyon.")
            print_slow("Surprisingly, you survive. But  only to be met with a giant cockroach.")
            fight1 = input("Do you want to *fight* or would you rather *run*?:  ")

            if "_compass_" in inventory:
                print_slow("#Tip: What would you do if it was a normal person?")

            if fight1 == "run":
                print("you instantly run, you find that there is a less steep hill nearby that can help you get back to the start of the dessert.")
            
            elif fight1 == "fight":
                if [[power >= 7] or [protection >= 7]] or fight1_2 != 1:
                    print("You fight until you don't have ay more energy even though the beast doesn't make a single move. The cockroach looks at you with sorrow and disappointment and leaves. You decide to go back a hill you find.")
                    fight1_2 = fight1_2 + 1
                
            elif fight1 == "talk":
                print_slow("Even though you see this unknown animal very frightening, you decided to gently hush in order to calm it down.")
                print_slow("The cockroach looks at you with confusion. To your surprise it responds and says 'What are you doing? I am the guardian of the Isoriac dessert. My unlucky body normally frightens most people but I'm actually very friendly!")
                print_slow("You discover that its name in Inorilarn and that he has been here since the first ray of light dried the sandy land. He hasn't talked to anyone in a lot of time as most adventurers are too terrified. It gives you a golden necklace as a reward and an orange orb that will help you incase you need his help.")
                print_slow("(This only  has three uses)")
                print_slow("After that, you decide to go back and decide that the rocks might have something useful.")
                inventory = inventory + "Inorilarn's-Orb_Light-Necklace_"
                power = power + 3
                ororb = int(1)
            else:
                print_slow("You have already been here.")
        else:
            stop_all()

elif dir1 == "forwards":
    print_slow("You are filled with a burning curiosity and decide to make headway for the mountain.")

elif dir1 == "right":
    print_slow("You decide that this is the best option for food and that you will be able to survive easily there.")

else:
    stop_all()
