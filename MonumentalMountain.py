from modules import health,protection,power,magic,inventory,clear,printSlow,msg,vowels,PowerUps,HashPassword
from story import places,msgs,NPCmsgs,secMsgs,Items,currentRoom
from intro import intro
# This is MonumentalMountain Alpha v0.0.3
# This "Alpha Game Program" (CC-BY-NO) was created by "Javier Fuentes-Hermoso"
# MonumentalMountain is licensed under the GNU GPLv3 license by ?, part of the J-A-I INNOVATIONS

clear()


introchoice = input("Would you like the introduction [Y/n]?:\t").title()
if introchoice == "Y" or introchoice == "Yes": name = intro()
else:
    name = input("You decide to refer to yourself as:\n>")
    print('\n')

timer = 0

TFmsgs = not True

while True:
    
    ## Start Turn
    #Print message
    clear()
    printSlow(f"{msg}\n\n")
    
    #This part slowly lowers your power and health as time passes, forcing you to eat and drink
    timer += 1
    if timer == 10:
        power -= 1
    if timer == 20:
        health -=1
        power -=1
        timer = 0
    if health <= 50 and health >= 45:
        printSlow("Your health is a bit low, you might want to heal by using a food or drink.")
    if health <= 40 and health >= 30:
        printSlow("Your health is quite low, you might want to heal by using a food or drink.")
    if health <= 20 and health >= 0:
        printSlow("Your health is very low, it is recomended that you heal as quick as possible.")

    #Print Room message unless option is turned off
    if TFmsgs == True:
        printSlow(msgs[currentRoom])
        print('\n'*2)
    
    #Display death message if health is zero or less
    if health <= 0:
        printSlow("Your health is 0 or less. You died.")
    
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

        nearbyItem = places[currentRoom]["Item"]

        if nearbyItem not in inventory and f"{currentRoom}-{nearbyItem}" not in PowerUps:

            if nearbyItem[-1] == 's' or nearbyItem == "Sand":
                printSlow(f"You see {nearbyItem}")

            elif nearbyItem[0] in vowels:
                printSlow(f"You see an {nearbyItem}")

            else:
                printSlow(f"You see a {nearbyItem}")
            print('\n')

    #Boss Checker
    if "Boss" in places[currentRoom].keys() and f"{places[currentRoom]['Boss']}bw" not in PowerUps:
        printSlow(f"You see a Boss {places[currentRoom]['Boss']}!\n")
    
    #NPC Checker
    if "NPC" in places[currentRoom].keys():
        printSlow(f"You see an NPC {places[currentRoom]['NPC']}\n")

    #Sign Chcker
    if "NPCS" in places[currentRoom].keys():
        printSlow(f"You see a sign {places[currentRoom]['NPCS']}\n")

    #Secret Checker
    if "Secret" in places[currentRoom].keys():
        if f"{places[currentRoom]['Secret']}s" not in PowerUps:
            realname = input("Please enter your real name:\n>")
            realnameHash = HashPassword(realname)
            print(realnameHash)
            if  realnameHash in places[currentRoom]['Secret']:
                print(secMsgs[currentRoom][realnameHash[-2:]])
            else: clear()
            PowerUps.append(f"{places[currentRoom]['Secret']}s")

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

                    if 'SingleUse' in Items[item]:
                        health += Items[item]['Buffs']["Health"]
                        protection += Items[item]['Buffs']["Protection"]
                        power += Items[item]['Buffs']["Power"]
                        magic += Items[item]['Buffs']["Magic"]
                        if Items[item]["SingleUse"]:
                            PowerUps.append(f"{currentRoom}-{nearbyItem}")

                else:
                    msg = f"You already have the {item}"
            
            else:
                msg = f"Can't find {item}"
        except:
           msg = f"Can't find {item}"
    
    #Player Statistics and Inventory
    elif action == "Stats":
        msg = f"\n\n{name}:\n\t Inventory: {inventory} \n\t Health: {health} \n\t Protection: {protection}\
\n\t Power: {power} \n\t Magic: {magic} \n\n"
    

    # Gives the compass messages
    elif action == "Use":
        if item in inventory:
            if 'SingleUse' in Items[item]:
                if Items[item]['msgt']:
                    msg = Items[item]['msg']
                else: msg = ''
                if Items[item]['SingleUse']:
                    inventory.remove(item)
                    PowerUps.append(item)
                    health += Items[item]['Buffs']["Health"]
                    protection += Items[item]['Buffs']["Protection"]
                    power += Items[item]['Buffs']["Power"]
                    magic += Items[item]['Buffs']["Magic"]
            else: msg = "You can't use that item"
        else: msg = f"You don't have the item \"{item}\""
    
    #Displays Help message with all available functions
    elif action == "Help":
        msg = "Possible actions:\n\tLook: Repeat prompt\n\tCompass: Get extra help if you need it\
\n\tStats: Print your stats\n\tHelp: Prints this\n\tYou can \"Go\":\n\t\tForewards\n\t\tBack\n\t\t\
Left\n\t\tRight\n\tYou can \"Get\" the item in the room that you are in if you don't already have it.\n\t\
You can \"Drop\" an item you have in your inventory\n\tYou can \"Use\" an Item if applicable\n\t\
You can \"Speak\" or \"Talk\" [Name of NPC] to talk with a Non-Playable Character, \
Do not use anything apart from initial keyword and the name of the NPC (This also works with bosses).\n\t\
You can \"Fight\" a boss in the room you are in\n\tAnd you can always \"Exit\"\n"
    
    #Reprints the current room message 
    elif action == "Look":
        TFmsgs = True
        continue

    #Talk with characters, NPCs or Bosses
    elif action == "Talk" or action == "Speak":
        if 'NPC' in places[currentRoom].keys() or 'Boss' in places[currentRoom].keys():
            if item == places[currentRoom]['NPC'] or item == places[currentRoom]['Boss']:
                msg = NPCmsgs['NPC'][item]['Conv']
                if 'PU' in NPCmsgs['NPC'][item]:
                    if f"NPCPU{item}" not in PowerUps:
                        health += NPCmsgs['NPC'][item]["PU"][0]
                        protection += NPCmsgs['NPC'][item]["PU"][1]
                        power += NPCmsgs['NPC'][item]["PU"][2]
                        magic += NPCmsgs['NPC'][item]["PU"][3]
                        if NPCmsgs['NPC']["PU"][item][3] not in inventory:
                            inventory.append(NPCmsgs['NPC'][item]["PU"][3])
                        PowerUps.append(f"NPCPU{item}")
            else: msg = f"Can't find \"{item}\" here."

   #Read signs 
    elif action == "Read":
        if 'NPCS' in places[currentRoom].keys():
            if item == places[currentRoom]['NPCS']:
                msg = NPCmsgs['NPCS'][item]['Tex']
            else: msg = f"Can't find the sign \"{item}\" here."
        else: print("There are no signs here.")
   

    #Fight Bosses
    elif action == "Fight":
        if "Boss" in places[currentRoom]:
            if f"{places[currentRoom]['Boss']}bw" not in PowerUps:
                if NPCmsgs["Bosses"][places[currentRoom]["Boss"]]["Req"][0] <= health and NPCmsgs["Bosses"][places[currentRoom]["Boss"]]["Req"][1] <= protection and NPCmsgs["Bosses"][places[currentRoom]["Boss"]]["Req"][2] <= power and NPCmsgs["Bosses"][places[currentRoom]["Boss"]]["Req"][3] <= magic and NPCmsgs["Bosses"][places[currentRoom]["Boss"]]["Req"][4] in inventory:
                    PowerUps.append(f"{places[currentRoom]['Boss']}bw")
                    msg = {NPCmsgs["Bosses"][places[currentRoom]["Boss"]]["FightWin"]}

                    PowerUps.append(currentRoom)
                    health += NPCmsgs['Bosses'][item]["Health"]
                    protection += NPCmsgs['Bosses'][item]["Protection"]
                    power += NPCmsgs['Bosses'][item]["Power"]
                    magic += NPCmsgs['Bosses'][item]["Magic"]
                    if NPCmsgs['Bosses'][item]["Item"] not in inventory:
                        inventory.append(NPCmsgs['Bosses'][item]["Item"])

                else:
                    msg = f"{NPCmsgs['Bosses'][places[currentRoom]['Boss']]['FightLose']}\nYour stats didn\'t meet the requirements to beat this Boss"

            else: msg = "You have allready fought this boss and they have despawned."
               
    elif action == "Drop":
        try:
            inventory.remove(item)
            msg = f"{item} has been removed from your inventory, you can retrieve it back from where you found it."
            
            if 'SingleUse' in Items[item]:
                health -= Items[item]['Buffs']["Health"]
                protection -= Items[item]['Buffs']["Protection"]
                power -= Items[item]['Buffs']["Power"]
                magic -= Items[item]['Buffs']["Magic"]
        except:
            msg = "You dont have that item"

    
    ##Debug commands
    #Prints your current room
    
    elif action == "Where":
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
        if item in places.keys():
            currentRoom = item
            msg = f'You are in {currentRoom}'
        else: msg = "No such place"

    elif action == "Pu":
        msg = PowerUps

    # Exit program
    elif action == "Exit":
        clear()
        printSlow('You have left the realm, see you later!')
        quit()

    # Any other commands invalid
    else:
        msg = "Invalid command\n"
