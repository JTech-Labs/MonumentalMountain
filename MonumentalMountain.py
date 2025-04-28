# SPDX-FileCopyrightText: (C) 2023-2025 jtech-labs <~jtech-labs/public@lists.sr.ht>
#
# SPDX-License-Identifier: MIT

from modules import *
from objects import *
from intro import intro
import linecache
# This is MonumentalMountain Alpha v0.0.4
# This Game Program was created by "Javier Fuentes-Hermoso"
# MonumentalMountain is licensed under the GNU GPLv3 license by Tinfoil Hat Studios, part of the J-A-I INNOVATIONS

# Get prefered language
story, ui = getStory()

#Define Items

#Setup the game and intro
def gameSetup():
    clear()

    #Ask if the user wants the introduction
    introchoice = input("Would you like the introduction [Y/n]?:\t").title()
    if introchoice == "Y" or introchoice == "Yes": name = intro()
    else:
        name = input("You decide to refer to yourself as:\n>")
        print('\n')


    timer = 0
    
    #Variable to see if the rooms message should be printed or not
    TFmsgs = not True

    return name, timer, TFmsgs, story

# Setup debug commands functions

# THE DEBUG COMMANDS - Work only if debugs have been enabled, which requires a secret password (the name Tilde is inspired by the key you press to bring up the Quake debug console)
def TildeKey(action: str,currentRoom: str,TFmsgs: bool,health: int,name: str,inventory: list):

    if "DebugEnabled" in PowerUps:

        #Prints your current room
        if action == "Where":
            msg = currentRoom

        #Changes option if you want ot see the current room message or not
        elif action == "Chngmsgs":
            TFmsgs = not TFmsgs
            msg = ''

        ##Change printSlow speed
        #elif action == "Sped":
            #sped = float(item)

        #Teleport
        elif action == "Tp":
            item2 = input("Input teleport target:\n>")
            if item2 in places:
                currentRoom2 = currentRoom
                currentRoom = item2
                msg = f'You you teleported from {currentRoom2} to {currentRoom}'
            else: msg = "No such place"

        elif action == "Pu":
            msg = PowerUps
        
        elif action == "Edithealth":
            health = int(input("Input new health amount:\n>"))
        
        elif action == "Chngname":
            name = input("Input new name:\n>")

        elif action == "Additem":
            inventory.append(input("Input item code:\n>"))

    # implement else with several randomly selected messages related to the misuse of dark magic
    else:
        msg = "Spell Unkown"
    return msg,currentRoom,TFmsgs,health,name,inventory

#Main function
if __name__ == "__main__":
    #Run Game Setup and initiate variables
    name,timer,TFmsgs = gameSetup()
    #Main game loop
    while True:
        
        ## Start Turn
        
        #Clear Screen
        clear()
        
        #Print the message
        printSlow(f"{msg}\n\n")

        #Display death message if health is zero or less
        if health <= 0:
            printSlow("Your health is 0 or less. You died.\n\nThanks for playing. You can always replay if you want, but your progress will not have been saved.")
            quit()
        
        #This part slowly lowers your power and health as time passes, forcing you to eat and drink
        timer += 1
        if timer == 10:
            power -= 1
        if timer == 20:
            health -=1
            power -=1
            timer = 0
        
        #Health Warnings        
        if health <= 50 and health >= 45:
            printSlow("Your health is a bit low, you might want to heal by using a food or drink.\n")
        if health <= 40 and health >= 30:
            printSlow("Your health is quite low, you might want to heal by using a food or drink.\n")
        if health <= 10 and health >= 0:
            printSlow("Your health is very low, it is recomended that you heal as quick as possible.\n")

        #Print Room message unless option is turned off
        if TFmsgs:
            
            with open("story.txt","r") as fi:
                for ln in fi:
                    if ln.startswith(currentRoom):
                        printSlow(ln.partition(': ')[-1])
                        break

            print('\n'*2)
        
        #Reset Buffs to zero if they are less than that
        if health > 100:
            health = 100
        
        if power < 0:
            power = 0
        
        if protection < 0:
            protection = 0
        
        if magic < 0:
            magic = 0
        
        ## Place Checkers

        # Item indicator
        if "Item" in places[currentRoom]:
                
                for theItemsInTheRoom in range(len(places[currentRoom]["Item"])):
                    if places[currentRoom]["Item"][theItemsInTheRoom] != "":
                        nearbyItem = places[currentRoom]["Item"][theItemsInTheRoom]

                        if nearbyItem not in inventory and f"{currentRoom}-{nearbyItem}" not in PowerUps:

                            if nearbyItem[-1] == 's' or nearbyItem == "Sand":
                                printSlow(f"You see {nearbyItem}")

                            elif nearbyItem[0] in vowels:
                                printSlow(f"You see an {nearbyItem}")

                            else:
                                printSlow(f"You see a {nearbyItem}")
                            print('\n')
                    else: break
        else: continue

        #Boss Checker
        if "Boss" in places[currentRoom] and f"{places[currentRoom]['Boss']}bw" not in PowerUps:
            printSlow(f"You see a Boss: {places[currentRoom]['Boss']}!\n")
        
        #NPC Checker
        if "NPC" in places[currentRoom]:
            printSlow(f"You see an NPC {places[currentRoom]['NPC']}\n")

        #Sign Chcker
        if "NPCS" in places[currentRoom]:
            printSlow(f"You see a sign {places[currentRoom]['NPCS']}\n")

        #Secret Checker
        if "Secret" in places[currentRoom]:
            if f"{currentRoom}Secret-s" not in PowerUps:
                realname = input("Please enter your real name:\n>")
                realnameHash = HashPassword(realname)
                #print(realnameHash)
                if realnameHash in places[currentRoom]['Secret']:
                    print(secMsgs[currentRoom][realnameHash])
                else: clear()
                PowerUps.append(f"{currentRoom}Secret-s")

        ## Player Moves

        # Accepts player's move as input
        userInput = input("\n\nEnter your move:\n> ")

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
            for idkanymore in range(len(item)):
                item[idkanymore] = item[idkanymore].title()
            
            item2 = " ".join(item)
            item = "".join(item)

        # Moving between places
        if action == "Go":
            if direction == "Back":
                direction = "Backwards"
            try:
                currentRoom = places[currentRoom][direction]
                #Each room can have a required item to pass, otherwise it will appear as if that isn't an available path
                if 'Req' in places[currentRoom]:
                    if places[currentRoom]['Req'] in inventory:
                        msg = f"You go {direction}"
                    else:
                        msg = "You can\'t go that way"
                        currentRoom = places[currentRoom]['Backwards']
                else: msg = f"You go {direction}"

            except KeyError:
                msg = "You can't go that way."

        # Picking up items
        elif action == "Get":
            try:
                if item2 in places[currentRoom]["Item"]:

                    if item not in inventory:
                        
                        #if len(item.split()) > 1: item = "".join(item.split())

                        inventory.append(item2)


                        msg = f"{item2} retrieved!"

                        item = theItems[f"{item}"]

                        if item.canBeUsed:
                        
                            if item.singleUse:
                                PowerUps.append(f"{currentRoom}-{nearbyItem}")
                            elif not item.singleUse:
                                health += item.health
                                protection += item.protection
                                power += item.power
                                magic += item.magic
                        else:
                            health += item.health
                            protection += item.protection
                            power += item.power
                            magic += item.magic

                    else:
                        msg = f"You already have the {item2}"
                
                else:
                    msg = f"Can't find {item2}"
            except KeyError:
                msg = f"Can't find {item2}"
        
        #Player Statistics and Inventory
        elif action == "Stats":
            msg = f"\n\n{name}:\n\t Inventory: {inventory} \n\t Health: {health} \n\t Protection: {protection}\
    \n\t Power: {power} \n\t Magic: {magic} \n\n"
        

        # Gives the compass messages
        elif action == "Use" or action == "Eat" or action == "Drink":
            
            if item == "Compass":
                compassMsg = story["Compass"][currentRoom]

            if item2 in inventory:
                item3 = item
                item = theItems[f"{item}"]
                if item.canBeUsed:
                    item.tip()
                    if item.singleUse:
                        inventory.remove(item2)
                        PowerUps.append(item)
                        health += item.health
                        protection += item.protection
                        power += item.power
                        magic += item.magic
                else: msg = f"You can't use the item \"{item2}\""
            else: msg = f"You don't have the item \"{item2}\""
        
        #Displays Help message with all available functions
        elif action == "Help":
            msg = "Possible actions:\n\tLook: Repeat prompt\n\tCompass: Get extra help if you need it\
    \n\tStats: Print your stats\n\tHelp: Prints this\n\tGo:\n\t\tForwards\n\t\tBackwards\n\t\t\
    Left\n\t\tRight\n\tGet: [The item you want if you don't already have it].\n\t\
    Drop: [Any item in your inventory]\n\tUse: [An Item in your inventory(if it is usable, use this instead of eat or drink)]\n\t\
    Speak/Talk: [Any NPC or character in that room (, \
    Do not use anything apart from initial keyword and the name of the NPC (This also works with bosses)).\n\t\
    Fight: [The boss in the room you are in]\n\tWhatis: [item] Gets the description of an item in your inventory\n\tAnd you can always \"Exit\"\n\nIf you need more help, plese see Features.md"
        
        #Reprints the current room message 
        elif action == "Look":
            TFmsgs = True
            msg = ""

        #Talk with characters, NPCs or Bosses
        elif action == "Talk" or action == "Speak":
            if 'NPC' in places[currentRoom]:
                if item == places[currentRoom]['NPC']:
                    #Check if the player can continuously speak with an NPC
                    if not f"NPCPU{item}" in PowerUps: # Remember to apply """ NPCmsgs['NPC'][item][5] """ for multiple different dialouges
                        # Get the Dialogue form the story.txt file
                        msg = story["NPCs"][f"{item}"]
                    else:
                        msg = f"{item2} is no longer here"
                    # Check if the player has already had a conversation with the NPC
                    if f"NPCPU{item}" not in PowerUps:
                        health += NPCmsgs['NPC'][item][0]
                        protection += NPCmsgs['NPC'][item][1]
                        power += NPCmsgs['NPC'][item][2]
                        magic += NPCmsgs['NPC'][item][3]
                        for itemAmount in NPCmsgs['NPC'][item][4]:
                            if NPCmsgs['NPC'][item][4][itemAmount] not in inventory:
                                inventory.append(NPCmsgs['NPC'][item][4][itemAmount])
                        PowerUps.append(f"NPCPU{item}")
                    else:
                        ''

            elif 'Boss' in places[currentRoom]:
                if item == places[currentRoom]['Boss']:
                    if f"NPCPU{item}" in PowerUps:
                        msg = story["NPCs"][f"{item2}-A"]
                    
                    elif f"{places[currentRoom]['Boss']}bw" in PowerUps:
                        msg = f"You have slain {item2}"

                    else:
                        msg = story["NPCs"][f"{item2}"]
                    if NPCmsgs['NPC'][item]:
                        if f"NPCPU{item}" not in PowerUps and f"{places[currentRoom]['Boss']}bw" not in PowerUps:
                            health += NPCmsgs['NPC'][item][0]
                            protection += NPCmsgs['NPC'][item][1]
                            power += NPCmsgs['NPC'][item][2]
                            magic += NPCmsgs['NPC'][item][3]
                            for itemAmount in range(len(NPCmsgs['NPC'][item][4])):
                                if NPCmsgs['NPC'][item][4][itemAmount] not in inventory:
                                    inventory.append(NPCmsgs['NPC'][item][4][itemAmount])
                            PowerUps.append(f"NPCPU{item}")
                else: msg = f"Can't find \"{item}\" to talk to here."
            else: msg = f"Can't find \"{item}\" to talk to here."

       #Read signs 
        elif action == "Read":
            if 'NPCS' in places[currentRoom].keys():
                if item == places[currentRoom]['NPCS']:
                    msg = story['NPCs'][f"item"]
                else: msg = f"Can't find the sign \"{item}\" here."
            else: print("There are no signs here.")

        #Fight Bosses or Enemys
        elif action == "Fight":
            try:
                if "Boss" in places[currentRoom]:
                    if item == places[currentRoom]['Boss']:
                        if f"{places[currentRoom]['Boss']}bw" not in PowerUps:
                            
                            doYouhavethatitem = True
                            doYouhavethatitemNum = 0
                            for doYouhavethatitemNum in range(len(NPCmsgs["Bosses"][places[currentRoom]["Boss"]][0][4])):
                                if NPCmsgs["Bosses"][places[currentRoom]["Boss"]][0][4][doYouhavethatitemNum] not in inventory:
                                    doYouhavethatitem = False
                                    break
                                else:
                                    continue
                            if doYouhavethatitem:
                                                    
                                if NPCmsgs["Bosses"][places[currentRoom]["Boss"]][0][0] <= health and NPCmsgs["Bosses"][places[currentRoom]["Boss"]][0][1] <= protection and NPCmsgs["Bosses"][places[currentRoom]["Boss"]][0][2] <= power and NPCmsgs["Bosses"][places[currentRoom]["Boss"]][0][3] <= magic:
                                    # Add support for several required items
                                    for gotThatItem in NPCmsgs["Bosses"][places[currentRoom]["Boss"]][0][4]:

                                        PowerUps.append(f"{places[currentRoom]['Boss']}bw")
                                        with open("story.txt","r") as fi:
                                            for ln in fi:
                                                if ln.startswith(f"Enemy- {item}-W"):
                                                    msg = ln.partition(': ')[-1]
                                                    break

                                        PowerUps.append(f"{places[currentRoom]['Boss']}bw")
                                        health += NPCmsgs['Bosses'][item][1][0]
                                        protection += NPCmsgs['Bosses'][item][1][1]
                                        power += NPCmsgs['Bosses'][item][1][2]
                                        magic += NPCmsgs['Bosses'][item][1][3]
                                        # Add support for several dropped items
                                        for gotThatItemNum in range(len(NPCmsgs['Bosses'][item][1][4])):
                                            if NPCmsgs['Bosses'][item][1][4][gotThatItemNum] not in inventory:
                                                inventory.append(NPCmsgs['Bosses'][item][1][4][gotThatItemNum])

                                else:
                                    story["Enemies"][f"{item}-L"]

                                    msg = f"{imsg}\nYour stats didn\'t meet the requirements to beat this Boss"
                            else:
                                story["Enemies"][f"{item}-L"]
                                
                                msg = f"{imsg}\nYour stats didn\'t meet the requirements to beat this Boss"

                        else: msg = "You have already fought this boss and they have despawned."
                    else:  msg = f"Can't find \"{item}\" here."

            except KeyError: msg = f"There is no {item} here"


        elif action == "Drop":
            try:
                inventory.remove(item)
                if item != "":
                    item = getattr(story, item)

                    if item.canBeUsed:
                        if item.singleUse:
                            msg = f"{item2} has been removed from your inventory, it breaks on the ground and dissapears, you can\'t get it back from where you found it."
                        elif not item.canBeUsed:
                            health -= item.health
                            protection -= item.protection
                            power -= item.power
                            magic -= item.magic
                            msg = f"{item2} has been removed from your inventory, you can retrieve it back from where you found it."

                    else:
                        health -= item.health
                        protection -= item.protection
                        power -= item.power
                        magic -= item.magic
                        msg = f"{item2} has been removed from your inventory, you can retrieve it back from where you found it."
                else: msg = "Please input a valid item"

            except ValueError:
                msg = f"You dont have the item \"{item2}\""

        elif action  == "Enabledebug":
            if "DebugDeleted" not in PowerUps and "DebugEnabled" not in PowerUps:
                realname = input("Please input the password (you have 1 try):\n>")
                realnameHash = HashPassword(realname)
                if realnameHash == "3435a27910d21fcb926190929fefaa20928d5052dd88adc75e153bb52d964345": PowerUps.append(f"DebugEnabled"); msg = "Dark Magic is not to be tampered with carelessly, use with extreme caution, and may the path of light always be there to guide you..."
                else: PowerUps.append("DebugDeleted")

        elif action == "Tilde":
            msg,currentRoom,TFmsgs,health,name,inventory = TildeKey(item,currentRoom,TFmsgs,health,name,inventory)

        elif action in debugList:
            if "DebugDeleted" not in PowerUps and "DebugEnabled" not in PowerUps:
                msg = "Spell Unkown"

        # Exit program
        elif action == "Exit":
            clear()
            printSlow('You have left the realm, see you later!')
            quit()

        # Any other commands invalid
        else:
            msg = "Invalid command\n"
