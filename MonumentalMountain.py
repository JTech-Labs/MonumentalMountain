from modules import health,protection,power,magic,inventory,clear,printSlow,msg,vowels
from story import places,msgs,compassMsgs,IS,NPCconvers
from intro import intro, name
clear()

introchoice = input("Would you like the introduction [Y/n]?:\t").title()
if introchoice == "Y": intro()
else: print('\n')

currentRoom = "Superliminal Space"

while True:

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
        msg = f"\n\n Inventory: {inventory} \n Health: {health} \n Protection: {protection}\
            \n Power: {power} \n Magic: {magic} \n\n"
    
    elif action == "Compass":
        if "compass" in inventory:
            msg = compassMsgs[currentRoom]
        else: msg = "You don't have a compass."
    
    elif action == "Help":
        msg = "Possible actions:\n\t Look: Repeat prompt\n\tCompass: Get extra help if you need it\
            \n\tStats: Print your stats\n\tHelp: Prints this\n\tYou can \"Go\":\n\t\tForewards\n\t\tBack\n\t\t\
            Left\n\t\tRight\n\tYou can \"Get\" the item in that room that you are in if you don't already have it.\n\t\
                And you can always \"Exit\""
    
    elif action == "Look": continue

    elif action == "Talk" or action == "Speak":
        if NPCconvers[currentRoom]["IS"] == True:
            print(f"Not yet implemented...")
        else: print("There is no one to talk to here.")

    # Exit program
    elif action == "Exit":
        msg = 'You have left the realm, see you later!'
        clear()
        quit()

    # Any other commands invalid
    else:
        msg = "Invalid command"
