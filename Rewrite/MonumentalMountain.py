from modules import *
import sys, time, random, os, webbrowser
from intro import intro

clear()
intro()

currentRoom = "Superliminal Space"

while True:

    clear()

    print(msg)

    print(msgs[currentRoom])

    # Item indicator
    if "Item" in rooms[currentRoom].keys():

        nearbyItem = rooms[currentRoom]["Item"]

        if nearbyItem not in inventory:

            if nearbyItem[-1] == 's':
                print(f"You see {nearbyItem}")

            elif nearbyItem[0] in vowels:
                print(f"You see an {nearbyItem}")

            else:
                print(f"You see a {nearbyItem}")
    
    ## Boss encounter
    #if "Boss" in rooms[currentRoom].keys():

        #if len(inventory) < 6:
            #print(f"You lost a fight with {rooms[currentRoom]['Boss']}.")
            #break

        #else:
            #print(f"You beat {rooms[currentRoom]['Boss']}!")
            #break

    # Accepts player's move as input
    userInput = input("Enter your move:\n")

    # Splits move into words
    nextMove = userInput.split(' ')

    # First word is action
    action = nextMove[0].title()

    # Reset item and direction
    item = "Item"
    direction = "null"

    # Second word is object or direction
    if len(nextMove) > 1:
        item = nextMove[1:]
        direction = nextMove[1].title()

        item = " ".join(item).title()

    # Moving between rooms
    if action == "Go":

        try:
            currentRoom = rooms[currentRoom][direction]
            msg = f"You go {direction}"

        except:
            msg = "You can't go that way."
    
    # Picking up items
    elif action == "Get":
        try:
            if item == rooms[currentRoom]["Item"]:

                if item not in inventory:

                    inventory.append(rooms[currentRoom]["Item"])
                    msg = f"{item} retrieved!"

                else:
                    msg = f"You already have the {item}"
            
            else:
                msg = f"Can't find {item}"
        except:
            msg = f"Can't find {item}"
    
    elif action == "Stats":
        print(f"\n\n Inventory: {inventory} \n Health: {health} \n Protection: {protection} \n Power: {power} \n Magic: {magic} \n\n")

    # Exit program
    elif action == "Exit":
        break

    # Any other commands invalid
    else:
        msg = "Invalid command"