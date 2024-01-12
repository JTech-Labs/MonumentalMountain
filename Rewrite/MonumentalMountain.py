import sys, time, random, os
from modules import clear, printSlow, health, protection, power, magic, inventory, places, vowels, msg, msgs
from intro import intro

clear()
intro()

currentRoom = "Superliminal Space"

while True:

    clear()

    printSlow(msg)

    printSlow(msgs[currentRoom])

    # Item indicator
    if "Item" in places[currentRoom].keys():

        nearbyItem = places[currentRoom]["Item"]

        if nearbyItem not in inventory:

            if nearbyItem[-1] == 's':
                printSlow(f"You see {nearbyItem}")

            elif nearbyItem[0] in vowels:
                printSlow(f"You see an {nearbyItem}")

            else:
                printSlow(f"You see a {nearbyItem}")
    
    ## Boss encounter
    #if "Boss" in places[currentRoom].keys():

        #if len(inventory) < 6:
            #printSlow(f"You lost a fight with {places[currentRoom]['Boss']}.")
            #break

        #else:
            #printSlow(f"You beat {places[currentRoom]['Boss']}!")
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

    # Moving between places
    if action == "Go":

        try:
            currentRoom = places[currentRoom][direction]
            msg = f"You go {direction}"

        except:
            msg = "You can't go that way."

    # Picking up items
    elif action == "Get":
        try:
            if item == places[currentRoom]["Item"]:

                if item not in inventory:

                    inventory.append(places[currentRoom]["Item"])
                    msg = f"{item} retrieved!"

                else:
                    msg = f"You already have the {item}"
            
            else:
                msg = f"Can't find {item}"
        except:
            msg = f"Can't find {item}"
    
    elif action == "Stats":
        printSlow(f"\n\n Inventory: {inventory} \n Health: {health} \n Protection: {protection}\
            \n Power: {power} \n Magic: {magic} \n\n")

    # Exit program
    elif action == "Exit":
        break

    # Any other commands invalid
    else:
        msg = "Invalid command"
